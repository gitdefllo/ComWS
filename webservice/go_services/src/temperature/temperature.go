package main

import (
    "fmt"
    "log"
    "net/http"
    "io/ioutil"
    "bytes"
    "xmlutil"
    "encoding/xml"
    "golang.org/x/net/html/charset"
)

type Envelope struct {
    Body `xml:"soap:"`
}

type Body struct {
    Msg interface{}
}

type GetWeather struct {
    CityName string
    CountryName string
}

var GetWeatherResponse struct {
    GetWeatherResult string
}

var CurrentWeather struct {
    Location string
    Time string
    Wind string
    Visibility string
    SkyConditions string
    Temperature string
    DewPoint string
    RelativeHumidity string
    Pressure string
    Status string
}

var xmlModel = bytes.NewBufferString(
    `<?xml version="1.0" encoding="utf-16"?> <CurrentWeather> <Location>Lyon / Bron, France (LFLY) 45-43N 004-57E 201M</Location> <Time>Jun 03, 2016 - 06:00 AM EDT / 2016.06.03 1000 UTC</Time> <Wind> Variable at 1 MPH (1 KT):0</Wind> <Visibility> greater than 7 mile(s):0</Visibility> <SkyConditions> overcast</SkyConditions> <Temperature> 62 F (17 C)</Temperature> <DewPoint> 53 F (12 C)</DewPoint> <RelativeHumidity> 72%</RelativeHumidity> <Pressure> 29.91 in. Hg (1013 hPa)</Pressure> <Status>Success</Status> </CurrentWeather>`)

func getWeather(city, country string) {
    x := xmlutil.NewXmlUtil()
    x.RegisterNamespace("http://www.w3.org/2001/XMLSchema-instance", "xsi")
    x.RegisterNamespace("http://www.w3.org/2001/XMLSchema", "xsd")
    x.RegisterNamespace("http://www.w3.org/2003/05/soap-envelope", "soap")
    x.RegisterTypeMore(Envelope{}, xml.Name{"http://www.w3.org/2003/05/soap-envelope", ""},
        []xml.Attr{
            xml.Attr{xml.Name{"xmlns", "xsi"}, "http://www.w3.org/2001/XMLSchema-instance"},
            xml.Attr{xml.Name{"xmlns", "xsd"}, "http://www.w3.org/2001/XMLSchema"},
            xml.Attr{xml.Name{"xmlns", "soap"}, "http://www.w3.org/2003/05/soap-envelope"},
        })
    x.RegisterTypeMore("", xml.Name{}, []xml.Attr{
        xml.Attr{xml.Name{"http://www.w3.org/2001/XMLSchema-instance", "type"}, "xsd:string"},
    })

    buf := new(bytes.Buffer)
    buf.WriteString(`<?xml version="1.0" encoding="utf-8"?>`)
    buf.WriteByte('\n')

    enc := x.NewEncoder(buf)
    env := &Envelope{ Body{ GetWeather{
        CityName: city,
        CountryName: country,
    }}}

    if err := enc.Encode(env); err != nil {
        log.Fatal(err)
    }

    // Print request
    bs := buf.Bytes()
    bs = bytes.Replace(bs, []byte{'>', '<'}, []byte{'>', '\n', '<'}, -1)
    fmt.Printf("%s\n\n", bs)

    // Send response, SOAP 1.2, fill in url, namespace, and action
    var r *http.Response
    url := "http://www.webservicex.net/"
    namespace := "globalweather"
    action := "GetWeather"
    r, fail := http.Post(url, "application/soap+xml; charset=utf-16; action="+namespace+"/"+action, buf)
    if fail != nil {
        return
    }
    // r.Body.Close()

    // Decode response
    decoder := xml.NewDecoder(r.Body)
    decoder = xml.NewDecoder(xmlModel)
    decoder.CharsetReader = charset.NewReaderLabel
    // err := decoder.Decode(&GetWeatherResponse)

    // decoder := x.NewDecoder(r.Body)
    // decoder = x.NewDecoder(xmlModel)
    
    // nr, err := charset.NewReaderLabel("utf-16", xmlModel)
    // if err != nil {
    //     panic(err)
    // }
    // dec := xml.NewDecoder(nr)

    // find := []xml.Name{
    //     xml.Name{"http://www.w3.org/2003/05/soap-envelope", "CurrentWeather"},
    //     xml.Name{"http://www.w3.org/2003/05/soap-envelope", "Fault"},
    // }

    fmt.Printf("------------\n")
    fmt.Printf("-----1------\n")
    fmt.Printf("------------\n")

    mbuf := new(bytes.Buffer)
    mbuf.ReadFrom(r.Body)
    fmt.Printf(mbuf.String() + "\n")

    fmt.Printf("------------\n")
    fmt.Printf("-----2------\n")
    fmt.Printf("------------\n")

    if b, err := ioutil.ReadAll(r.Body); err == nil {
        fmt.Printf(string(b) + "\n")
    }

    fmt.Printf("------------\n")
    fmt.Printf("-----3------\n")
    fmt.Printf("------------\n")

    if err := decoder.Decode(&CurrentWeather); err != nil {
        fmt.Printf("err: %v\n", err)
    }
    
    fmt.Printf("%s\n", CurrentWeather)

    // if start.Name.Local == "Fault" {
    //     log.Fatal("Fault!") // Here you can decode a Soap Fault
    // }

    // var resp CurrentWeather
    // if err := decoder.DecodeElement(&resp, start); err != nil {
    //     log.Fatal(err)
    // }

    // fmt.Printf("%#v\n\n", resp)
}

func main() {
    getWeather("Lyon", "France")
}