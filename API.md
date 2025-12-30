# Balanz Requests Examples

## Init

```bash
curl 'https://clientes.balanz.com/api/v1/auth/init?avoidAuthRedirect=true' \
 -H 'sec-ch-ua-platform: "macOS"' \
 -H 'Lang: es' \
 -H 'Referer: https://clientes.balanz.com/auth/login?t=1766976892042' \
 -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
 -H 'Accept: application/json' \
 -H 'content-type: application/json' \
 --data-raw '{"user":"fulano","source":"WebV2"}'
```

```bash
{
    "tipoAutenticacion": 0,
    "user": "fulano",
    "URLAuth": "",
    "nonce": "3E27568B-61EF-45EB-9C96-5B77582DC8D8"
}
```

## Login

```bash
curl 'https://clientes.balanz.com/api/v1/auth/login?avoidAuthRedirect=true' \
 -H 'accept: application/json' \
 -H 'accept-language: es-419,es;q=0.9,en;q=0.8' \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' \
 -b 'cookiesession1=678ADAB8D279A8C720C7EFE6CD176282; _ga_KQY8GBM085=GS2.2.s1761531772$o1$g0$t1761531772$j60$l0$h0; _ga=GA1.1.201650615.1761526178; _ga_XT4Q9ZDDZ6=GS2.1.s1762917073$o5$g0$t1762917079$j54$l0$h311494586' \
 -H 'lang: es' \
 -H 'origin: https://clientes.balanz.com' \
 -H 'pragma: no-cache' \
 -H 'priority: u=1, i' \
 -H 'referer: https://clientes.balanz.com/auth/login?t=1766976892042' \
 -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 -H 'sec-fetch-dest: empty' \
 -H 'sec-fetch-mode: cors' \
 -H 'sec-fetch-site: same-origin' \
 -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
 --data-raw '{"user":"fulano","pass":"xxxxxxxx","nonce":"3E27568B-61EF-45EB-9C96-5B77582DC8D8","source":"WebV2","idDispositivo":"935e71e3-afca-4b12-afed-79a9c75da7f0","TipoDispositivo":"Web","sc":1,"Nombre":"Mac OS 10.15.7 Chrome 142.0.0.0","SistemaOperativo":"Mac OS","VersionSO":"10.15.7","VersionAPP":"2.30.9"}'
```

```bash
{
  "idAplicacion": 1,
  "idProductor": null,
  "idPersona": "109521",
  "Nombre": "Lopez, Fulano",
  "idSesion": "258965571",
  "AccessToken": "AECF2DA4-38ED-4C82-8090-77E5CA99C3DF",
  "Avatar": "/api/v1/avatar/avt_3B06FE3CDEC4A79A2248B9DFB2DF1E574B014CAF.jpg",
  "email": "fulano@gmail.com",
  "TipoDocumento": "1",
  "Documento": "123456789",
  "TelefonoFijo": "",
  "TelefonoMovil": "**********3060",
  "tieneC4D": "1",
  "CaraRegistrada": null,
  "CUIL": "201234567892",
  "UltimoLogin": "28/12/2025 23:57:19",
  "EsMenor": "0",
  "user": "fulano",
}
```

# Logout

```bash
curl 'https://clientes.balanz.com/api/v1/logout' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'Authorization: B4496985-B788-4BAC-A328-84AFBC3863C4' \
  -H 'Lang: es' \
  -H 'Referer: https://clientes.balanz.com/app/mi-cartera' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'Accept: application/json' \
  -H 'content-type: application/json' \
  --data-raw '{}'
````


# Estado de cuenta


```bash
curl 'https://clientes.balanz.com/api/v1/estadodecuenta/103340?Fecha=20251229&ta=1&idMoneda=1' \
 -H 'sec-ch-ua-platform: "macOS"' \
 -H 'Authorization: AECF2DA4-38ED-4C82-8090-77E5CA99C3DF' \
 -H 'Lang: es' \
 -H 'Referer: https://clientes.balanz.com/app/mi-cartera' \
 -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
 -H 'Accept: application/json' \
 -H 'content-type: application/json'
```


```bash
{
  "tenenciaAgrupada": [
    {
      "valorTotal": 1522230,
      "Cantidad": 4,
      "Tipo": "Bonos",
      "detalle": [
        {
          "orden": 10,
          "idMoneda": 1,
          "Moneda": "Pesos",
          "ValorActual": 1522230,
          "VariacionPorcentual": 0,
          "VariacionAbsoluta": 0,
          "Rendimiento": 0,
          "NoRealizado": 298249,
          "Cantidad": 4,
          "idMonedaValuacion": 1
        }
      ],
      "idTipoInstrumento": 2,
      "Color": "#097C6F"
    },
    {
      "valorTotal": 15356538,
      "Cantidad": 13,
      "detalle": [
        {
          "orden": 14,
          "idMoneda": 1,
          "Moneda": "Pesos",
          "ValorActual": 14730818,
          "VariacionPorcentual": 0,
          "VariacionAbsoluta": 0,
          "Rendimiento": 0,
          "NoRealizado": 602545,
          "Cantidad": 12,
          "idMonedaValuacion": 1
        },
        {
          "orden": 14,
          "idMoneda": 2,
          "Moneda": "Dólares",
          "ValorActual": 421,
          "VariacionPorcentual": 0,
          "VariacionAbsoluta": 0,
          "Rendimiento": 0,
          "NoRealizado": 32,
          "Cantidad": 1,
          "idMonedaValuacion": 2
        }
      ],
      "Tipo": "Corporativos",
      "idTipoInstrumento": 16,
      "Color": "#59B964"
    },
    {
      "valorTotal": 2610745,
      "Cantidad": 5,
      "detalle": [
        {
          "orden": 20,
          "idMoneda": 1,
          "Moneda": "Pesos",
          "ValorActual": 2610745,
          "VariacionPorcentual": 0,
          "VariacionAbsoluta": 0,
          "Rendimiento": 0,
          "NoRealizado": 624561,
          "Cantidad": 5,
          "idMonedaValuacion": 1
        }
      ],
      "Tipo": "Acciones",
      "idTipoInstrumento": 1,
      "Color": "#FDD651"
    },
    {
      "valorTotal": 23361455,
      "Cantidad": 17,
      "detalle": [
        {
          "orden": 25,
          "idMoneda": 1,
          "Moneda": "Pesos",
          "ValorActual": 23361455,
          "VariacionPorcentual": 0,
          "VariacionAbsoluta": 0,
          "Rendimiento": 0,
          "NoRealizado": 1396486,
          "Cantidad": 17,
          "idMonedaValuacion": 1
        }
      ],
      "Tipo": "Cedears",
      "idTipoInstrumento": 12,
      "Color": "#CFDB38"
    },
    {
      "valorTotal": 348527,
      "Cantidad": 1,
      "detalle": [
        {
          "orden": 30,
          "idMoneda": 2,
          "Moneda": "Dólares",
          "ValorActual": 235,
          "VariacionPorcentual": 0,
          "VariacionAbsoluta": 0,
          "Rendimiento": 0,
          "NoRealizado": 1,
          "Cantidad": 1,
          "idMonedaValuacion": 2
        }
      ],
      "Tipo": "Fondos",
      "idTipoInstrumento": 13,
      "Color": "#9BD660"
    }
  ],
  "tenencia": [
    {
      "Tipo": "Bonos",
      "Ticker": "AL35",
      "idMoneda": 1,
      "Grilla": 1,
      "Moneda": "Dólares",
      "Descripcion": "BONO REP. ARGENTINA USD STEP UP 2035",
      "Cantidad": 100,
      "Disponible": 100,
      "Garantias": 0,
      "Precio": 1145.6,
      "PPP": 826.8,
      "ValorInicial": 82680,
      "ValorActual": 114560,
      "ValorActualPesos": 114560,
      "PorcTenencia": 0.26,
      "NoRealizado": 31880,
      "PorcRendimiento": 38.56,
      "TNA": "213.24%",
      "Variacion": "=0.00 (0.00%)",
      "PrecioAnterior": 1145.6,
      "FechaUltimoOperado": "26/12/2025",
      "DiasPromedioTenencia": 66,
      "panel": 6
    },
    {
      "Tipo": "Corporativos",
      "Ticker": "CS48O",
      "idMoneda": 1,
      "Grilla": 1,
      "Moneda": "Dólares",
      "Descripcion": "ON CRESUD S32 CL48 V11/07/28 U$S CG",
      "Cantidad": 1473,
      "Disponible": 1473,
      "Garantias": 0,
      "Precio": 1585,
      "PPP": 1610.1,
      "ValorInicial": 2371677,
      "ValorActual": 2334705,
      "ValorActualPesos": 2334705,
      "PorcTenencia": 5.27,
      "NoRealizado": -36972,
      "PorcRendimiento": -1.56,
      "TNA": "-8.62%",
      "Variacion": "=0.00 (0.00%)",
      "PrecioAnterior": 1585,
      "FechaUltimoOperado": "26/12/2025",
      "DiasPromedioTenencia": 66,
      "panel": 16
    },
    {
      "Tipo": "Acciones",
      "Ticker": "CEPU",
      "idMoneda": 1,
      "Grilla": 1,
      "Moneda": "Pesos",
      "Descripcion": "CENTRAL PUERTO S.A. ESCRIT. \"B\" 1 V.",
      "Cantidad": 180,
      "Disponible": 180,
      "Garantias": 0,
      "Precio": 2712.5,
      "PPP": 2150.8,
      "ValorInicial": 387144,
      "ValorActual": 488250,
      "ValorActualPesos": 488250,
      "PorcTenencia": 1.1,
      "NoRealizado": 101106,
      "PorcRendimiento": 26.12,
      "TNA": "301.31%",
      "Variacion": "=0.00 (0.00%)",
      "PrecioAnterior": 2712.5,
      "FechaUltimoOperado": "26/12/2025",
      "DiasPromedioTenencia": 31.64,
      "panel": 4
    },
    {
      "Tipo": "Cedears",
      "Ticker": "ASML",
      "idMoneda": 1,
      "Grilla": 1,
      "Moneda": "Pesos",
      "Descripcion": "CEDEAR ASML HOLDING NV",
      "Cantidad": 83,
      "Disponible": 83,
      "Garantias": 0,
      "Precio": 11350,
      "PPP": 10995.57639759,
      "ValorInicial": 912633,
      "ValorActual": 942050,
      "ValorActualPesos": 942050,
      "PorcTenencia": 2.13,
      "NoRealizado": 29417,
      "PorcRendimiento": 3.22,
      "TNA": "17.83%",
      "Variacion": "=0.00 (0.00%)",
      "PrecioAnterior": 11350,
      "FechaUltimoOperado": "26/12/2025",
      "DiasPromedioTenencia": 66,
      "panel": 7
    },
    {
      "Tipo": "Fondos",
      "Ticker": "ESTRA1A",
      "idMoneda": 2,
      "Grilla": 2,
      "Moneda": "Dólares",
      "Descripcion": "Dolar Corto Plazo Clase A",
      "Cantidad": 208.27,
      "Disponible": 208.27,
      "Garantias": 0,
      "Precio": 1.126246,
      "PPP": 1.122841,
      "ValorInicial": 234,
      "ValorActual": 235,
      "ValorActualPesos": 348526.74,
      "PorcTenencia": 0.79,
      "NoRealizado": 1,
      "PorcRendimiento": 0.3,
      "TNA": "10.06%",
      "Variacion": "=0.00 (0.00%)",
      "PrecioAnterior": 1.126246,
      "FechaUltimoOperado": "26/12/2025",
      "DiasPromedioTenencia": 11,
      "panel": 10,
      "BaseTicker": "ESTRA1"
    }
  ],
  "liquidez": [
    {
      "idMoneda": 1,
      "Moneda": "Pesos",
      "Simbolo": "$",
      "DInm": 1022039.67,
      "DOInm": 1022039.67,
      "FInm": "29/12/2025",
      "D24": 1022039.67,
      "DO24": 1022039.67,
      "F24": "30/12/2025",
      "D48": 1022039.67,
      "DO48": 1022039.67,
      "F48": "02/01/2026",
      "D72": 1022039.67,
      "DO72": 1022039.67,
      "F72": "05/01/2026",
      "DFut": 1022039.67,
      "DOFut": 1022039.67,
      "Cotizacion": 1,
      "DO": 1022039.67
    },
    {
      "idMoneda": 2,
      "Moneda": "Dólares",
      "Simbolo": "u$s",
      "DInm": 30.88,
      "DOInm": 30.88,
      "FInm": "29/12/2025",
      "D24": 30.88,
      "DO24": 30.88,
      "F24": "30/12/2025",
      "D48": 30.88,
      "DO48": 30.88,
      "F48": "02/01/2026",
      "D72": 30.88,
      "DO72": 30.88,
      "F72": "05/01/2026",
      "DFut": 30.88,
      "DOFut": 30.88,
      "Cotizacion": 1485.88,
      "DO": 30.88
    },
    {
      "idMoneda": 4,
      "Moneda": "US Dollar (Cable)",
      "Simbolo": "usd",
      "DInm": 0.38,
      "DOInm": 0.38,
      "FInm": "29/12/2025",
      "D24": 0.38,
      "DO24": 0.38,
      "F24": "30/12/2025",
      "D48": 0.38,
      "DO48": 0.38,
      "F48": "02/01/2026",
      "D72": 0.38,
      "DO72": 0.38,
      "F72": "05/01/2026",
      "DFut": 0.38,
      "DOFut": 0.38,
      "Cotizacion": 1527.17,
      "DO": 0.38
    }
  ],
  "tenenciaActual": [
    {
      "TotalPesos": 44267998,
      "Total": 44267998,
      "TotalAnterior": 44267998,
      "Movimientos": 0,
      "Instrumentos": 43199494,
      "InstrumentosPesos": 42225248,
      "InstrumentosDolares": 656,
      "Monedas": 1067923.64,
      "SimboloMoneda": "$",
      "Disponible": 0,
      "VariacionAbs": 0,
      "VariacionRel": 0,
      "TextoCotizacionDolar": "Dólar MEP: $ <b>1.485,88</b> | Dólar Cable: $ <b>1.527,17</b>",
      "CotizacionMEP": 1485.88,
      "CotizacionCCL": 1527.17
    }
  ]
}
```

## Rendimiento

```bash
curl 'https://clientes.balanz.com/api/v1/evoluciondecartera/103340?FechaDesde=20250929&FechaHasta=20251229&idMoneda=2&Tenencia=1&Eventos=1' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'Authorization: 5AB7486B-2919-4457-A5F8-FCA2F60F0768' \
  -H 'Lang: es' \
  -H 'Referer: https://clientes.balanz.com/app/detalle' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'Accept: application/json' \
  -H 'content-type: application/json'
```


```bash
{
  "resumen": [
    {
      "id": 1,
      "Nombre": "Valor Inicial",
      "Rango": 35.15,
      "1M": 27282.97,
      "3M": 35.15,
      "6M": 0,
      "YTD": 0,
      "12M": 0
    },
    {
      "id": 2,
      "Nombre": "Monto Operado",
      "Rango": 2839.45,
      "1M": 1594.34,
      "3M": 2839.45,
      "6M": 11634.63,
      "YTD": 11634.63,
      "12M": 11634.63
    },
    {
      "id": 3,
      "Nombre": "Instrumentos Operados",
      "Rango": -2839.45,
      "1M": -1594.34,
      "3M": -2839.45,
      "6M": -11634.63,
      "YTD": -11634.63,
      "12M": -11634.63
    },
    {
      "id": 4,
      "Nombre": "Depositos/Suscripciones",
      "Rango": 2670.67,
      "1M": 1837.42,
      "3M": 2670.67,
      "6M": 7112.77,
      "YTD": 7112.77,
      "12M": 7112.77
    },
    {
      "id": 5,
      "Nombre": "Extracciones/Rescates",
      "Rango": 0,
      "1M": 0,
      "3M": 0,
      "6M": -4315.97,
      "YTD": -4315.97,
      "12M": -4315.97
    },
    {
      "id": 6,
      "Nombre": "Dividendos",
      "Rango": 38.15,
      "1M": 33.53,
      "3M": 38.15,
      "6M": 38.15,
      "YTD": 38.15,
      "12M": 38.15
    },
    {
      "id": 7,
      "Nombre": "Cupones",
      "Rango": 90.58,
      "1M": 60.83,
      "3M": 90.58,
      "6M": 90.58,
      "YTD": 90.58,
      "12M": 90.58
    },
    {
      "id": 8,
      "Nombre": "Gastos",
      "Rango": -49.45,
      "1M": -41.49,
      "3M": -49.45,
      "6M": -92.03,
      "YTD": -92.03,
      "12M": -92.03
    },
    {
      "id": 9,
      "Nombre": "Ajustes",
      "Rango": -2.9,
      "1M": -2.64,
      "3M": -2.9,
      "6M": -2.9,
      "YTD": -2.9,
      "12M": -2.9
    },
    {
      "id": 10,
      "Nombre": "Títulos Transferidos Recibidos",
      "Rango": 24120.57,
      "1M": 0,
      "3M": 24120.57,
      "6M": 24120.57,
      "YTD": 24120.57,
      "12M": 24120.57
    },
    {
      "id": 11,
      "Nombre": "Títulos Transferidos Enviados",
      "Rango": 0,
      "1M": 0,
      "3M": 0,
      "6M": 0,
      "YTD": 0,
      "12M": 0
    },
    {
      "id": 13,
      "Nombre": "Resultado por Tenencia",
      "Rango": 2889.68,
      "1M": 621.81,
      "3M": 2889.68,
      "6M": 2841.28,
      "YTD": 2841.28,
      "12M": 2841.28
    },
    {
      "id": 14,
      "Nombre": "Valor Final",
      "Rango": 29792.43,
      "1M": 29792.43,
      "3M": 29792.43,
      "6M": 29792.43,
      "YTD": 29792.43,
      "12M": 29792.43
    },
    {
      "id": 15,
      "Nombre": "Cambio en el Valor de la Cuenta",
      "Rango": 29757.28,
      "1M": 2509.47,
      "3M": 29757.28,
      "6M": 29792.43,
      "YTD": 29792.43,
      "12M": 29792.43
    },
    {
      "id": 16,
      "Nombre": "Cambio en el Valor de la Cuenta (%)",
      "Rango": 84646.74,
      "1M": 9.2,
      "3M": 84646.74,
      "6M": 0,
      "YTD": 0,
      "12M": 0
    }
  ],
  "rendimiento": [
    {
      "Fecha": "29/09/2025",
      "Rendimiento": -3.1,
      "RendimientoAbs": -1.72
    },
    {
      "Fecha": "30/09/2025",
      "Rendimiento": -3.56,
      "RendimientoAbs": -0.25
    },
    {
      "Fecha": "01/10/2025",
      "Rendimiento": -1.06,
      "RendimientoAbs": 1.38
    },
    {
      "Fecha": "02/10/2025",
      "Rendimiento": -1.55,
      "RendimientoAbs": -0.27
    },
    {
      "Fecha": "03/10/2025",
      "Rendimiento": -1.16,
      "RendimientoAbs": 0.22
    }
  ],
  "tenencia": [
    {
      "Fecha": "02/09/2025",
      "Tenencia": 36.35,
      "Dolares": 35.57,
      "Pesos": 0.78,
      "Bonos": 0,
      "FCI": 0,
      "Acciones": 0,
      "Monedas": 0.78,
      "MonedasPesos": 0.78,
      "MonedasDolares": 0,
      "Opciones": 0
    },
    {
      "Fecha": "03/09/2025",
      "Tenencia": 36.46,
      "Dolares": 35.69,
      "Pesos": 0.78,
      "Bonos": 0,
      "FCI": 0,
      "Acciones": 0,
      "Monedas": 0.78,
      "MonedasPesos": 0.78,
      "MonedasDolares": 0,
      "Opciones": 0
    },
    {
      "Fecha": "04/09/2025",
      "Tenencia": 36.31,
      "Dolares": 35.54,
      "Pesos": 0.76,
      "Bonos": 0,
      "FCI": 0,
      "Acciones": 0,
      "Monedas": 0.76,
      "MonedasPesos": 0.76,
      "MonedasDolares": 0,
      "Opciones": 0
    },
    {
      "Fecha": "05/09/2025",
      "Tenencia": 37.47,
      "Dolares": 36.7,
      "Pesos": 0.77,
      "Bonos": 0,
      "FCI": 0,
      "Acciones": 0,
      "Monedas": 0.77,
      "MonedasPesos": 0.77,
      "MonedasDolares": 0,
      "Opciones": 0
    },
    {
      "Fecha": "08/09/2025",
      "Tenencia": 36.94,
      "Dolares": 36.2,
      "Pesos": 0.75,
      "Bonos": 0,
      "FCI": 0,
      "Acciones": 0,
      "Monedas": 0.75,
      "MonedasPesos": 0.75,
      "MonedasDolares": 0,
      "Opciones": 0
    }
  ],
  "eventos": [
    {
      "date": "22/12/2025",
      "type": "pin",
      "backgroundColor": "#FF8080",
      "graph": "graph1",
      "text": "CC",
      "description": "Boleto / 12585025 / APCOLCON / 0 / $ 1020000.00"
    },
    {
      "date": "22/12/2025",
      "type": "pin",
      "backgroundColor": "#FF8080",
      "graph": "graph1",
      "text": "CF",
      "description": "Boleto / 12585026 / APCOLFUT / 1 / $ 1020701.42"
    },
    {
      "date": "19/12/2025",
      "type": "pin",
      "backgroundColor": "#FF8080",
      "graph": "graph1",
      "text": "CF",
      "description": "Boleto / 12534800 / APCOLFUT / 3 / $ 1021743.78"
    },
    {
      "date": "19/12/2025",
      "type": "pin",
      "backgroundColor": "#FF8080",
      "graph": "graph1",
      "text": "CC",
      "description": "Boleto / 12534799 / APCOLCON / 0 / $ 1020000.00"
    },
    {
      "date": "19/12/2025",
      "type": "arrowUp",
      "backgroundColor": "#00CC00",
      "graph": "graph1",
      "text": "D",
      "description": "+$1017477"
    },
    {
      "date": "18/12/2025",
      "type": "arrowUp",
      "backgroundColor": "#00CC00",
      "graph": "graph1",
      "text": "D",
      "description": "+u$s139"
    }
  ]
}
``

## Flujo de fondos proyectado

```bash
curl 'https://clientes.balanz.com/api/v1/bonos/flujoproyectado/103340' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'Authorization: 6F8CA355-60B6-4F6E-9139-4A1DFD0DAD8C' \
  -H 'Lang: es' \
  -H 'Referer: https://clientes.balanz.com/app/mi-cartera?openinstrument=Cedears&action_from=mis-instrumentos-home' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'Accept: application/json' \
  -H 'content-type: application/json'
```

```bash
{
    "tabla": [
        {
            "descripcionbono": "IRSA Inversiones y Representaciones S.A. - Clase XXIV - Dolares - (IR2PO Adicionales) - USP58809BU07",
            "codigoespeciebono": "IRCPO",
            "tenencia": 1471,
            "precio": 1550,
            "tir": "7.73%",
            "tna": "7.45%",
            "spread": "",
            "duration": 5.88,
            "int_corr": 2,
            "prox_pago": "2026-03-31",
            "vto": "2035-03-31",
            "amort": "Sinkable",
            "frec_pago": "Sem",
            "cuponbono": "Tasa Fija: 8.000%",
            "residual": "100.00%",
            "obsprox_pago": "Renta",
            "tipo_moneda": 2,
            "tipo": "TASA FIJA",
            "currentyield": "7.81%",
            "paridad": "102.43%",
            "diasrestantes": 3331,
            "grupo_cupon": "Tasa Fija",
            "descripcion_moneda": "DOLARES"
        },
        {
            "descripcionbono": "Telecom Argentina - Clase 21 - Dolares - USP9028NBT74",
            "codigoespeciebono": "TLCMO",
            "tenencia": 1000,
            "precio": 1685,
            "tir": "7.19%",
            "tna": "6.95%",
            "spread": "",
            "duration": 3.56,
            "int_corr": 4.275,
            "prox_pago": "2026-01-18",
            "vto": "2031-07-18",
            "amort": "Sinkable",
            "frec_pago": "Sem",
            "cuponbono": "Tasa Fija: 9.500%",
            "residual": "100.00%",
            "obsprox_pago": "Renta",
            "tipo_moneda": 2,
            "tipo": "TASA FIJA",
            "currentyield": "8.69%",
            "paridad": "108.92%",
            "diasrestantes": 1998,
            "grupo_cupon": "Tasa Fija",
            "descripcion_moneda": "DOLARES"
        },
    ],
    "excluidos": [],
    "flujo": [
        {
            "codigoespeciebono": "GD35",
            "fecha": "2026-01-09",
            "vr": 100,
            "renta": 19.8,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 19.8,
            "tipo_moneda": 2
        },
        {
            "codigoespeciebono": "AL35",
            "fecha": "2026-01-09",
            "vr": 100,
            "renta": 2.063,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 2.063,
            "tipo_moneda": 2
        },
        {
            "codigoespeciebono": "CS48O",
            "fecha": "2026-01-11",
            "vr": 100,
            "renta": 59.404,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 59.404,
            "tipo_moneda": 2
        },
        {
            "codigoespeciebono": "YM34O",
            "fecha": "2026-01-17",
            "vr": 100,
            "renta": 60.968,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 60.968,
            "tipo_moneda": 2
        },
        {
            "codigoespeciebono": "TLCMO",
            "fecha": "2026-01-18",
            "vr": 100,
            "renta": 47.5,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 47.5,
            "tipo_moneda": 2
        },
        {
            "codigoespeciebono": "YM38O",
            "fecha": "2026-01-22",
            "vr": 100,
            "renta": 4.424,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 4.424,
            "tipo_moneda": 2
        },
        {
            "codigoespeciebono": "DNC5O",
            "fecha": "2026-02-05",
            "vr": 100,
            "renta": 18.677,
            "amort": 0,
            "rentaamort": "Renta",
            "total": 18.677,
            "tipo_moneda": 2
        },
    ]
}
```