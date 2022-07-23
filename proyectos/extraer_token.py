def run():
  
  lista_result = ["""]=Juan+Ramirez&card[number]=4381086470232737&card[cvc]=473&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:16 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 5e895b19-fa5f-4b4e-b3d0-6ac5c420eb3e
Original-Request: req_DX2SF5JVyEcXUH
Request-Id: req_DX2SF5JVyEcXUH
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4WEAXIGNKSo5LelqvVXN",
  "object": "token",
  "card": {
    "id": "card_1LDx4WEAXIGNKSo5gtwFFjKg",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "2737",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017776,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420715864&card[cvc]=487&card[exp_month]=10&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:17 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0190aa8f-5cfa-4745-a647-5cc955a8ebd8
Original-Request: req_Pudgvw8MbzB2o7
Request-Id: req_Pudgvw8MbzB2o7
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4XEAXIGNKSo5szSMuQP9",
  "object": "token",
  "card": {
    "id": "card_1LDx4XEAXIGNKSo5UIYIHKw6",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5864",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017777,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425104528&card[cvc]=768&card[exp_month]=07&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:18 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: eb7ef33f-c177-4264-81a9-53cf0db78d5a
Original-Request: req_BEXGr1m2U4vsHV
Request-Id: req_BEXGr1m2U4vsHV
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4YEAXIGNKSo5pUql4Cxb",
  "object": "token",
  "card": {
    "id": "card_1LDx4YEAXIGNKSo5lsXUGpvH",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4528",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017778,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:18 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415532431&card[cvc]=026&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:19 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a9f0bb5e-471d-42ab-bbfb-9755044536f2
Original-Request: req_JJ1QZZ9qCCOZ4O
Request-Id: req_JJ1QZZ9qCCOZ4O
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4ZEAXIGNKSo5QF3h9fC3",
  "object": "token",
  "card": {
    "id": "card_1LDx4ZEAXIGNKSo5n9HeFhJ7",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "2431",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017779,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:19 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411061344&card[cvc]=628&card[exp_month]=06&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:20 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d3187622-d4db-444a-a38d-5503c220d63c
Original-Request: req_Syif37j1Usoqtw
Request-Id: req_Syif37j1Usoqtw
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4aEAXIGNKSo5sDvBX4Av",
  "object": "token",
  "card": {
    "id": "card_1LDx4aEAXIGNKSo5MGDfdKms",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "1344",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017780,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:20 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432851830&card[cvc]=504&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:21 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f95a7eea-c7a7-4bcb-abad-ebb56b7c1c25
Original-Request: req_cV6E4AgFfFKvVC
Request-Id: req_cV6E4AgFfFKvVC
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4bEAXIGNKSo5hRg9JTiW",
  "object": "token",
  "card": {
    "id": "card_1LDx4bEAXIGNKSo5iJOPNcwl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "1830",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017781,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:21 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427002845&card[cvc]=371&card[exp_month]=04&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:22 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 37974139-47e7-42e2-9a13-04f0b176327f
Original-Request: req_OOCrlG2xh8jOwF
Request-Id: req_OOCrlG2xh8jOwF
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4cEAXIGNKSo5aFvGxuSW",
  "object": "token",
  "card": {
    "id": "card_1LDx4cEAXIGNKSo5aGBVEck8",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2845",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017782,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:22 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431133347&card[cvc]=763&card[exp_month]=02&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:23 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d971f6a1-4402-4558-8067-2335980f47d9
Original-Request: req_pUkfSImdRvkn69
Request-Id: req_pUkfSImdRvkn69
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4dEAXIGNKSo5BkoCY1zR",
  "object": "token",
  "card": {
    "id": "card_1LDx4dEAXIGNKSo5Ez95VmXN",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "3347",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017783,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:23 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086416252005&card[cvc]=008&card[exp_month]=04&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:24 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 90cc2fde-594f-4ff3-9c94-0b21bc2acafd
Original-Request: req_e0YkhcU26lszs6
Request-Id: req_e0YkhcU26lszs6
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4eEAXIGNKSo5c54WVQsE",
  "object": "token",
  "card": {
    "id": "card_1LDx4eEAXIGNKSo5J2fFdxDH",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2005",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017784,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:24 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433338431&card[cvc]=827&card[exp_month]=07&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:25 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 89b81870-1eb8-4e99-ab68-5e809645b947
Original-Request: req_FeKCAGmtyitYeF
Request-Id: req_FeKCAGmtyitYeF
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4fEAXIGNKSo56iBNonBt",
  "object": "token",
  "card": {
    "id": "card_1LDx4fEAXIGNKSo5ia6GkZ5f",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8431",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017785,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:26 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430653444&card[cvc]=201&card[exp_month]=04&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:27 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d3812cdb-0978-4367-aca0-66520359992b
Original-Request: req_4fFjHKeVfKMh3m
Request-Id: req_4fFjHKeVfKMh3m
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4gEAXIGNKSo54JbNrvV4",
  "object": "token",
  "card": {
    "id": "card_1LDx4gEAXIGNKSo567A5xdYf",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3444",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017786,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:27 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424686442&card[cvc]=208&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:28 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7ff320ab-8f0b-469c-8b08-6e6f2f148fa3
Original-Request: req_Forryb1sNX3szp
Request-Id: req_Forryb1sNX3szp
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4iEAXIGNKSo5VhWMlCBf",
  "object": "token",
  "card": {
    "id": "card_1LDx4hEAXIGNKSo5Z16CTIv6",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "6442",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017788,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:28 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432172674&card[cvc]=267&card[exp_month]=03&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:29 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 373e10c6-e187-4e36-a363-eb8d455a774f
Original-Request: req_J3EbJJDQzpn5wQ
Request-Id: req_J3EbJJDQzpn5wQ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4jEAXIGNKSo5jrbg7Jrh",
  "object": "token",
  "card": {
    "id": "card_1LDx4iEAXIGNKSo5tMbVagIq",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "2674",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017789,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412545865&card[cvc]=727&card[exp_month]=11&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:30 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 8e034917-f3b0-4202-ad50-8cb9ee7994fe
Original-Request: req_f7ohjxsSdZY9pP
Request-Id: req_f7ohjxsSdZY9pP
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4kEAXIGNKSo5lWhYxY6L",
  "object": "token",
  "card": {
    "id": "card_1LDx4kEAXIGNKSo5EuJ3rb5I",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5865",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017790,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:31 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433740578&card[cvc]=274&card[exp_month]=12&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:31 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: be3f9b2a-c6bf-45fa-9986-ee5e359dead1
Original-Request: req_a5LigY6b06i26G
Request-Id: req_a5LigY6b06i26G
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4lEAXIGNKSo5MreMEa1f",
  "object": "token",
  "card": {
    "id": "card_1LDx4lEAXIGNKSo5fBjRSdhf",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0578",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017791,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:32 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086404020125&card[cvc]=625&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:33 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: cc4accc0-ee4e-4581-9e73-661e6690972b
Original-Request: req_PzUXr70mrJ48KP
Request-Id: req_PzUXr70mrJ48KP
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4nEAXIGNKSo5XgQV9Mre",
  "object": "token",
  "card": {
    "id": "card_1LDx4nEAXIGNKSo5z5EJCRD9",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0125",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017793,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:34 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412280646&card[cvc]=017&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:34 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: da58aeb2-b043-43a7-9304-80e13802b0cb
Original-Request: req_i1p4jlD8T0nICC
Request-Id: req_i1p4jlD8T0nICC
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4oEAXIGNKSo5Ktcpp5Jz",
  "object": "token",
  "card": {
    "id": "card_1LDx4oEAXIGNKSo5zYCCsMNF",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "0646",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017794,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:35 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425580131&card[cvc]=674&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:36 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 95349c90-c81f-4ab2-8917-0401ffda6c87
Original-Request: req_jyONoWE1B8JOwe
Request-Id: req_jyONoWE1B8JOwe
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4qEAXIGNKSo5IKc6bbwW",
  "object": "token",
  "card": {
    "id": "card_1LDx4qEAXIGNKSo5fPAjBaMg",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "0131",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017796,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:37 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086406433615&card[cvc]=642&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:38 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 57f60268-fd8b-4a33-bd80-ec41dfe319e6
Original-Request: req_QcpnOi0W7Dfm24
Request-Id: req_QcpnOi0W7Dfm24
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4sEAXIGNKSo5j8LjIB6B",
  "object": "token",
  "card": {
    "id": "card_1LDx4rEAXIGNKSo54N7eNFsl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3615",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017798,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:38 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432011526&card[cvc]=180&card[exp_month]=07&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:39 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0c060f98-05c7-4f70-bb25-e130c7031b52
Original-Request: req_jQytNXmKVIQWmK
Request-Id: req_jQytNXmKVIQWmK
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4tEAXIGNKSo5ktE7SdIo",
  "object": "token",
  "card": {
    "id": "card_1LDx4tEAXIGNKSo5AgqvxNSu",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1526",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017799,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:40 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432588325&card[cvc]=077&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:41 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 3489b4f8-6075-4580-a4a5-a80f9384c79d
Original-Request: req_0YDR30bRQdYXsG
Request-Id: req_0YDR30bRQdYXsG
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4vEAXIGNKSo5UphlwFZj",
  "object": "token",
  "card": {
    "id": "card_1LDx4uEAXIGNKSo5U2umSxCl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8325",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017801,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:42 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426077657&card[cvc]=642&card[exp_month]=06&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:42 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 64f6b5b5-7a59-4252-ae19-0d92f27881d0
Original-Request: req_9fLvfwG1keOOiU
Request-Id: req_9fLvfwG1keOOiU
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4wEAXIGNKSo58WsG1wzP",
  "object": "token",
  "card": {
    "id": "card_1LDx4wEAXIGNKSo5hsq3cb5b",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "7657",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017802,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:43 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086413513300&card[cvc]=741&card[exp_month]=06&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:44 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 64513f78-81f5-4c43-8b20-4743de510102
Original-Request: req_vwWURK5qslbCuo
Request-Id: req_vwWURK5qslbCuo
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx4yEAXIGNKSo5XB91pmdk",
  "object": "token",
  "card": {
    "id": "card_1LDx4yEAXIGNKSo5ajYlZXMh",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3300",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017804,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:45 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434386405&card[cvc]=616&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:46 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 517cba53-67da-40d6-8d88-e5b0fb6d2fc1
Original-Request: req_1HwPt3AD6Wvfpw
Request-Id: req_1HwPt3AD6Wvfpw
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx50EAXIGNKSo5XOfvr5sz",
  "object": "token",
  "card": {
    "id": "card_1LDx4zEAXIGNKSo5ClGqSizR",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "6405",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017806,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:47 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086407760032&card[cvc]=501&card[exp_month]=11&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:47 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0ceb0754-81c0-4307-9bdf-c9f482d27518
Original-Request: req_7yvaX4XDZUuAWB
Request-Id: req_7yvaX4XDZUuAWB
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx51EAXIGNKSo5NkiLUZBg",
  "object": "token",
  "card": {
    "id": "card_1LDx51EAXIGNKSo5Yak7iXbU",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "0032",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017807,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:48 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427661038&card[cvc]=888&card[exp_month]=11&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:49 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 163c3cb7-187d-4260-99ea-d1e503392077
Original-Request: req_WGBHdPi0vmjGto
Request-Id: req_WGBHdPi0vmjGto
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx53EAXIGNKSo5wDz0HijS",
  "object": "token",
  "card": {
    "id": "card_1LDx53EAXIGNKSo50Iil158v",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1038",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017809,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:50 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430534032&card[cvc]=643&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:51 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9624e9b0-d0e3-478e-8fd4-6fe7cb2f0ce9
Original-Request: req_KbeiGybkcJI8g9
Request-Id: req_KbeiGybkcJI8g9
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx55EAXIGNKSo5ovQ7Q6gm",
  "object": "token",
  "card": {
    "id": "card_1LDx55EAXIGNKSo5wk8f8SvT",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4032",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017811,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:52 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431708577&card[cvc]=185&card[exp_month]=06&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:53 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c249bcfd-ce79-4af5-90d0-158a7f4242ac
Original-Request: req_aleOZhs0URbS5b
Request-Id: req_aleOZhs0URbS5b
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx57EAXIGNKSo57fVbr6vT",
  "object": "token",
  "card": {
    "id": "card_1LDx57EAXIGNKSo5aSaWIvah",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8577",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017813,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:54 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430187047&card[cvc]=568&card[exp_month]=10&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:55 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0918aec7-62d8-43b3-8f6d-27a33f843599
Original-Request: req_XPsRBKcV3bAqHH
Request-Id: req_XPsRBKcV3bAqHH
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx59EAXIGNKSo5xKqZgFbc",
  "object": "token",
  "card": {
    "id": "card_1LDx59EAXIGNKSo5DIXoLfa6",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "7047",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017815,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:56 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420212110&card[cvc]=664&card[exp_month]=12&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:57 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 108aef82-3789-4d4e-9763-bf3a2ae50848
Original-Request: req_ojUzFzCcj857EP
Request-Id: req_ojUzFzCcj857EP
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5BEAXIGNKSo5OmjbRS99",
  "object": "token",
  "card": {
    "id": "card_1LDx5BEAXIGNKSo5TuviZlqq",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2110",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017817,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:56:58 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415625003&card[cvc]=151&card[exp_month]=03&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:56:59 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d2acdaf0-7c62-423d-b906-60282c641f9d
Original-Request: req_haXzOhmx9bPQ8K
Request-Id: req_haXzOhmx9bPQ8K
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5DEAXIGNKSo5tlo2JNiY",
  "object": "token",
  "card": {
    "id": "card_1LDx5DEAXIGNKSo5Sp8f9vPG",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5003",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017819,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:00 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086408142560&card[cvc]=463&card[exp_month]=11&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:01 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 792c0bbf-ca76-41b5-b1e8-24f1ca184ad0
Original-Request: req_BvJSxrTrL9wSEL
Request-Id: req_BvJSxrTrL9wSEL
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5FEAXIGNKSo5YE3gi4o4",
  "object": "token",
  "card": {
    "id": "card_1LDx5FEAXIGNKSo5AkLC8PZy",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2560",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017821,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:03 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414013763&card[cvc]=131&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:03 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 5b424788-793d-4c4d-a0e5-29b41358e9fe
Original-Request: req_uI68N0VrZlnqld
Request-Id: req_uI68N0VrZlnqld
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5HEAXIGNKSo5nHVNd3st",
  "object": "token",
  "card": {
    "id": "card_1LDx5HEAXIGNKSo508vZGWej",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "3763",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017823,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:05 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086410544365&card[cvc]=781&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:06 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 1da21fb9-2fc5-445a-a119-7daf919c4b35
Original-Request: req_x1R4L0id264yGM
Request-Id: req_x1R4L0id264yGM
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5KEAXIGNKSo5jlOvb8Ea",
  "object": "token",
  "card": {
    "id": "card_1LDx5KEAXIGNKSo5LfZb63zM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4365",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017826,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:07 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431005305&card[cvc]=574&card[exp_month]=11&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:08 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: cf188865-2abd-4f2d-a662-df4bd8867eaa
Original-Request: req_nbLvElCetV3kXk
Request-Id: req_nbLvElCetV3kXk
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5MEAXIGNKSo5OpNJCjgk",
  "object": "token",
  "card": {
    "id": "card_1LDx5MEAXIGNKSo5Uq9cykuG",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5305",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017828,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:09 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412251167&card[cvc]=210&card[exp_month]=03&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:10 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0d23b93f-7e9c-4d5c-b076-ee722a2207e2
Original-Request: req_qucbn4RZs45VpS
Request-Id: req_qucbn4RZs45VpS
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5OEAXIGNKSo53PyzMRvz",
  "object": "token",
  "card": {
    "id": "card_1LDx5OEAXIGNKSo5rUloNO9z",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1167",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017830,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:12 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431548106&card[cvc]=715&card[exp_month]=03&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:13 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0f2fd66d-30a7-425c-a31a-580a66d91c78
Original-Request: req_CTFjxnRGDwoRuI
Request-Id: req_CTFjxnRGDwoRuI
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5REAXIGNKSo5PpmUy8L5",
  "object": "token",
  "card": {
    "id": "card_1LDx5QEAXIGNKSo5zD2YNBT9",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "8106",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017833,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:14 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412262701&card[cvc]=707&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:15 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 82365599-019b-4a6f-a4c7-29b150d06b62
Original-Request: req_Vnh1q0kXWnjLT8
Request-Id: req_Vnh1q0kXWnjLT8
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5TEAXIGNKSo5l8bcWkPe",
  "object": "token",
  "card": {
    "id": "card_1LDx5TEAXIGNKSo5ZhmJFoQ3",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "2701",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017835,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086403877582&card[cvc]=455&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:18 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ef735f45-9855-424c-bf9d-1494a3e0a9a9
Original-Request: req_ynSGV9SE91hB9C
Request-Id: req_ynSGV9SE91hB9C
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5WEAXIGNKSo5MUXntcaK",
  "object": "token",
  "card": {
    "id": "card_1LDx5VEAXIGNKSo5KX0NzVWr",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "7582",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017838,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:19 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086403065352&card[cvc]=324&card[exp_month]=03&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:20 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c5bbdf96-f961-4aa7-be29-74c312a10391
Original-Request: req_xrMoFaLNtitVdf
Request-Id: req_xrMoFaLNtitVdf
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5YEAXIGNKSo5zRbjuloz",
  "object": "token",
  "card": {
    "id": "card_1LDx5YEAXIGNKSo5De7Me7nL",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5352",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017840,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:22 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086416710614&card[cvc]=156&card[exp_month]=04&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:23 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c9e42ab6-5129-40bb-b433-e6d37a44cedd
Original-Request: req_Wc6jztPDIOlujB
Request-Id: req_Wc6jztPDIOlujB
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5bEAXIGNKSo5ZuXWgDe2",
  "object": "token",
  "card": {
    "id": "card_1LDx5aEAXIGNKSo54U5z3YxX",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "0614",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017843,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:24 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427144340&card[cvc]=078&card[exp_month]=01&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:25 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 26fdd270-93c5-4b64-98f7-4937649c3e6d
Original-Request: req_iW6Y3RamNaaoPP
Request-Id: req_iW6Y3RamNaaoPP
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5dEAXIGNKSo50QHWnt25",
  "object": "token",
  "card": {
    "id": "card_1LDx5dEAXIGNKSo58bFcFpe0",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4340",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017845,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:26 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086416615763&card[cvc]=861&card[exp_month]=02&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:27 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 03e1db0f-ffa5-4b17-b82f-b081ef29ab33
Original-Request: req_1gIOsK566XQFvP
Request-Id: req_1gIOsK566XQFvP
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5fEAXIGNKSo5uqcLqQWe",
  "object": "token",
  "card": {
    "id": "card_1LDx5fEAXIGNKSo5mJo6lg2k",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "5763",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017847,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433083342&card[cvc]=353&card[exp_month]=04&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:30 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 00f8daa5-60f0-4dfa-9366-182c328c4196
Original-Request: req_kztu8ic7JQQREA
Request-Id: req_kztu8ic7JQQREA
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5hEAXIGNKSo59W0nSkFZ",
  "object": "token",
  "card": {
    "id": "card_1LDx5hEAXIGNKSo5B3gr2euD",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3342",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017849,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:31 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433826583&card[cvc]=624&card[exp_month]=11&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:32 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f5238c0b-5694-4c91-9d30-0cfb8a470642
Original-Request: req_12WroMuKtQYGnU
Request-Id: req_12WroMuKtQYGnU
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5kEAXIGNKSo5RcBVARJr",
  "object": "token",
  "card": {
    "id": "card_1LDx5kEAXIGNKSo5k4YbbEb2",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6583",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017852,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:33 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434123337&card[cvc]=507&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:34 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e873737f-6c19-4c98-9d73-c507c40bca20
Original-Request: req_GXhpbj3cnXzKGb
Request-Id: req_GXhpbj3cnXzKGb
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5mEAXIGNKSo5T3fEO2TR",
  "object": "token",
  "card": {
    "id": "card_1LDx5mEAXIGNKSo5UUbF5iex",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "3337",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017854,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:36 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433222767&card[cvc]=223&card[exp_month]=06&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:37 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6358434e-45e3-448b-9dfd-28b76176b932
Original-Request: req_R8hf4KpVl5FqJZ
Request-Id: req_R8hf4KpVl5FqJZ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5pEAXIGNKSo52kFLgShr",
  "object": "token",
  "card": {
    "id": "card_1LDx5oEAXIGNKSo5cw8pLbtE",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2767",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017857,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:38 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422564807&card[cvc]=731&card[exp_month]=10&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:39 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: fa50e573-0ae2-4351-b62c-f58d865a170c
Original-Request: req_bBK6wc1Z4Htoqz
Request-Id: req_bBK6wc1Z4Htoqz
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5rEAXIGNKSo5IKYQhDnI",
  "object": "token",
  "card": {
    "id": "card_1LDx5rEAXIGNKSo5J4kXTgd1",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "4807",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017859,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:41 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427576087&card[cvc]=810&card[exp_month]=10&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:42 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6911634a-76b2-4c81-9248-eb4b25878c30
Original-Request: req_lSZkumJNdzhrSu
Request-Id: req_lSZkumJNdzhrSu
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5uEAXIGNKSo5bIliilcD",
  "object": "token",
  "card": {
    "id": "card_1LDx5tEAXIGNKSo5jpfKsCef",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "6087",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017862,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:43 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422208686&card[cvc]=435&card[exp_month]=12&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:44 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: fe54f369-c0d4-47dd-a2ea-4f41ad9ea1ad
Original-Request: req_NuhuWDjWqBQlD4
Request-Id: req_NuhuWDjWqBQlD4
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5wEAXIGNKSo5JPu9neuq",
  "object": "token",
  "card": {
    "id": "card_1LDx5wEAXIGNKSo5lsyqoLU5",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8686",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017864,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:46 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433141751&card[cvc]=450&card[exp_month]=03&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:47 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a3186561-928d-4ea6-a1e7-fdd567a71ef1
Original-Request: req_jOCJtiEmKEN13n
Request-Id: req_jOCJtiEmKEN13n
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx5zEAXIGNKSo5Jtv5vmx9",
  "object": "token",
  "card": {
    "id": "card_1LDx5zEAXIGNKSo5GzsmxLEn",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1751",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017867,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:49 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431676428&card[cvc]=762&card[exp_month]=11&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:50 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e1ea04b5-e976-441f-b9ae-d58594351b06
Original-Request: req_RoA2Nb1SK1zjRr
Request-Id: req_RoA2Nb1SK1zjRr
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx61EAXIGNKSo59fVLkB08",
  "object": "token",
  "card": {
    "id": "card_1LDx61EAXIGNKSo5tvxMmAZM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "6428",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017869,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:51 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086418835864&card[cvc]=753&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:52 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ac355f96-52d1-41c0-8c67-d33a6f0edec3
Original-Request: req_tN02UOpPqsNsbK
Request-Id: req_tN02UOpPqsNsbK
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx64EAXIGNKSo5xvtuXmao",
  "object": "token",
  "card": {
    "id": "card_1LDx64EAXIGNKSo5Ep71BERM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5864",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017872,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:54 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411872377&card[cvc]=255&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:55 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 4a8c33e0-fe37-4b5d-9501-e7f97fcb5469
Original-Request: req_T5pYBO85T1rcqN
Request-Id: req_T5pYBO85T1rcqN
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx67EAXIGNKSo5WkpX1MwJ",
  "object": "token",
  "card": {
    "id": "card_1LDx67EAXIGNKSo5127fTWYy",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2377",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017875,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:57 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086403853385&card[cvc]=403&card[exp_month]=12&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:57:58 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a5c92848-9859-4070-9a00-2b25fff30a2c
Original-Request: req_BRg4AASLoNn5Kg
Request-Id: req_BRg4AASLoNn5Kg
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6AEAXIGNKSo5ltJWVK50",
  "object": "token",
  "card": {
    "id": "card_1LDx69EAXIGNKSo519vsaMWm",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "3385",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017878,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:57:59 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424477560&card[cvc]=408&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:00 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 04701624-dad9-4e15-a07d-d0aed81a761d
Original-Request: req_Bh89o60LTW8PQq
Request-Id: req_Bh89o60LTW8PQq
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6CEAXIGNKSo5PuZGtXZL",
  "object": "token",
  "card": {
    "id": "card_1LDx6CEAXIGNKSo5BXntA9s1",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "7560",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017880,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:02 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431814854&card[cvc]=016&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:03 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6fc32417-03fe-4779-bb65-23d6c287f2b4
Original-Request: req_gcqjlxNS4zdlYp
Request-Id: req_gcqjlxNS4zdlYp
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6FEAXIGNKSo5iNPfxuS0",
  "object": "token",
  "card": {
    "id": "card_1LDx6FEAXIGNKSo50vpWn5Fa",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "4854",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017883,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:05 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415802057&card[cvc]=768&card[exp_month]=01&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:06 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a6d5b78c-d54c-43e7-9e0d-0079e6b390a6
Original-Request: req_MCfezAbgYpBRej
Request-Id: req_MCfezAbgYpBRej
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6IEAXIGNKSo5H1Eoqdim",
  "object": "token",
  "card": {
    "id": "card_1LDx6IEAXIGNKSo5z1w5uACn",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2057",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017886,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:08 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428038137&card[cvc]=682&card[exp_month]=07&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:09 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 65967f74-b822-4f08-be84-86b5346680e4
Original-Request: req_TK1yEpvv8Dm4MR
Request-Id: req_TK1yEpvv8Dm4MR
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6LEAXIGNKSo56zk9ApmA",
  "object": "token",
  "card": {
    "id": "card_1LDx6LEAXIGNKSo5CsQZfi0u",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8137",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017889,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:11 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414513887&card[cvc]=115&card[exp_month]=01&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:12 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6cb3d590-a0da-4f39-97a6-fbfb4a89a075
Original-Request: req_BodbAEP6dJSXHH
Request-Id: req_BodbAEP6dJSXHH
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6OEAXIGNKSo5y5809YkG",
  "object": "token",
  "card": {
    "id": "card_1LDx6NEAXIGNKSo5Tcmzk7M0",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "3887",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017892,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:14 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086404331100&card[cvc]=044&card[exp_month]=05&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:15 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: bb476266-d9a0-4671-a1b2-3d3e7f69062d
Original-Request: req_fXA7iTyeNYiRTh
Request-Id: req_fXA7iTyeNYiRTh
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6REAXIGNKSo55eXfsJke",
  "object": "token",
  "card": {
    "id": "card_1LDx6QEAXIGNKSo5nmpRTS2k",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "1100",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017895,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414120113&card[cvc]=736&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:18 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e6da0cb0-ee54-41b4-a0d0-2227b1ff7739
Original-Request: req_NK8gckHp31ghYO
Request-Id: req_NK8gckHp31ghYO
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6UEAXIGNKSo5SNPVOoGw",
  "object": "token",
  "card": {
    "id": "card_1LDx6TEAXIGNKSo5LBTUn5zf",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0113",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017898,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:20 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425505716&card[cvc]=756&card[exp_month]=02&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:21 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c1164a5f-9faf-43c7-b1ff-f8b352f7a6f8
Original-Request: req_GN6mawq8XtfMbf
Request-Id: req_GN6mawq8XtfMbf
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6XEAXIGNKSo55wEFNZbx",
  "object": "token",
  "card": {
    "id": "card_1LDx6WEAXIGNKSo5i8CbiyCI",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5716",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017901,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:23 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411310824&card[cvc]=846&card[exp_month]=02&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:24 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: dc33a101-1086-4304-bb9b-feb351ea7c57
Original-Request: req_ngcuAuEuwq3CJl
Request-Id: req_ngcuAuEuwq3CJl
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6aEAXIGNKSo5EIuoLAFV",
  "object": "token",
  "card": {
    "id": "card_1LDx6ZEAXIGNKSo5DebOQORu",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "0824",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017904,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:26 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086423178375&card[cvc]=145&card[exp_month]=11&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:27 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 3b6bb029-5b54-4a95-96b5-44a044830589
Original-Request: req_VO4PuMShpsaBV0
Request-Id: req_VO4PuMShpsaBV0
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6dEAXIGNKSo5XfdUOPX6",
  "object": "token",
  "card": {
    "id": "card_1LDx6dEAXIGNKSo5uznZj29g",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "8375",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017907,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422631721&card[cvc]=358&card[exp_month]=05&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:30 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9dbdee65-b064-4057-a8e0-3d2c99588a3d
Original-Request: req_zrLEI5OZUSqDjr
Request-Id: req_zrLEI5OZUSqDjr
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6gEAXIGNKSo5QSxhshQY",
  "object": "token",
  "card": {
    "id": "card_1LDx6gEAXIGNKSo53qcB5Kz4",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "1721",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017910,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:32 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415547561&card[cvc]=517&card[exp_month]=11&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:33 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 26ccc194-4a38-4b79-92ee-d76b539d362a
Original-Request: req_zgrB6iHyauirHf
Request-Id: req_zgrB6iHyauirHf
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6jEAXIGNKSo59Bpu89S9",
  "object": "token",
  "card": {
    "id": "card_1LDx6jEAXIGNKSo5TGTRldPa",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "7561",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017913,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:35 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431835545&card[cvc]=066&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:36 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f5bcf86c-8d8a-4c82-b5d1-4b4bcad58eb4
Original-Request: req_sipcp4vjao5Szw
Request-Id: req_sipcp4vjao5Szw
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6mEAXIGNKSo5EEVQgyu6",
  "object": "token",
  "card": {
    "id": "card_1LDx6mEAXIGNKSo5Vx201G02",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5545",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017916,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:39 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086417688322&card[cvc]=445&card[exp_month]=12&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:40 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 973a5c60-ad56-4d39-ac24-91b0f3f87dbb
Original-Request: req_yX9Lp8AfX03v9T
Request-Id: req_yX9Lp8AfX03v9T
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6qEAXIGNKSo5gcFqevW2",
  "object": "token",
  "card": {
    "id": "card_1LDx6pEAXIGNKSo5KLyOWNgp",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8322",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017920,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:42 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426137634&card[cvc]=435&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:43 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 1f83bea6-4cbf-4137-9d6e-622d0e863a46
Original-Request: req_OiKyLLfijxByOn
Request-Id: req_OiKyLLfijxByOn
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6tEAXIGNKSo56z7DeCbf",
  "object": "token",
  "card": {
    "id": "card_1LDx6tEAXIGNKSo5u78HkmzJ",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "7634",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017923,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:45 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086423878818&card[cvc]=640&card[exp_month]=11&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:46 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 37e83da1-1f39-4586-8646-0b5af4fdda41
Original-Request: req_3eelFi5uByKMtx
Request-Id: req_3eelFi5uByKMtx
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx6wEAXIGNKSo5L1ytGlYc",
  "object": "token",
  "card": {
    "id": "card_1LDx6wEAXIGNKSo5zo1CFO1e",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8818",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017926,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:49 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431661222&card[cvc]=468&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:50 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 812399a8-3142-42ce-981b-fe7f2f1fb467
Original-Request: req_D2BDgkLp3ehdoh
Request-Id: req_D2BDgkLp3ehdoh
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx70EAXIGNKSo5tEqDNi9j",
  "object": "token",
  "card": {
    "id": "card_1LDx6zEAXIGNKSo5qdCJTjkP",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1222",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017930,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:52 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086413700725&card[cvc]=436&card[exp_month]=06&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:53 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7154a6a8-f0ee-4f67-b0fb-067427ce568e
Original-Request: req_5MtqXffztdppbb
Request-Id: req_5MtqXffztdppbb
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx73EAXIGNKSo5N0TJyDEe",
  "object": "token",
  "card": {
    "id": "card_1LDx73EAXIGNKSo57s5FPbMh",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0725",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017933,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:55 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086402030506&card[cvc]=406&card[exp_month]=10&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:58:56 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e886d4ac-5fa7-465c-ab29-42b33fe01673
Original-Request: req_MTKgsw7bHIO2oZ
Request-Id: req_MTKgsw7bHIO2oZ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx76EAXIGNKSo5bCVdIM4N",
  "object": "token",
  "card": {
    "id": "card_1LDx76EAXIGNKSo5DceG8MLD",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0506",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017936,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:58:59 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420632085&card[cvc]=730&card[exp_month]=07&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:00 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ac34f47f-b45d-4952-a34c-0cfcb28bccb3
Original-Request: req_PsVlEql0Mk29p4
Request-Id: req_PsVlEql0Mk29p4
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7AEAXIGNKSo53I4H8PGt",
  "object": "token",
  "card": {
    "id": "card_1LDx7AEAXIGNKSo5MK8pUwGQ",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "2085",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017940,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:02 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424183127&card[cvc]=156&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:03 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9922ef89-eb19-4456-9865-5c8cb5e23454
Original-Request: req_n2coP3eV9rEtJ8
Request-Id: req_n2coP3eV9rEtJ8
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7DEAXIGNKSo5PdpsxjRz",
  "object": "token",
  "card": {
    "id": "card_1LDx7DEAXIGNKSo5v65ybGJO",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "3127",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017943,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:06 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420441222&card[cvc]=167&card[exp_month]=07&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:07 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0948fb32-e00f-4e97-959e-f5664f91a686
Original-Request: req_qMJzgQKE2UYFM8
Request-Id: req_qMJzgQKE2UYFM8
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7HEAXIGNKSo5ZU4yzNsJ",
  "object": "token",
  "card": {
    "id": "card_1LDx7HEAXIGNKSo5ldDOlMGE",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1222",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017947,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:09 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434070603&card[cvc]=626&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:11 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: de2df594-d7ce-463a-af35-573e528cb735
Original-Request: req_iCbCSbYuWKcbyl
Request-Id: req_iCbCSbYuWKcbyl
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7KEAXIGNKSo5tkPaYTDS",
  "object": "token",
  "card": {
    "id": "card_1LDx7KEAXIGNKSo5j5KFdcCe",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0603",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017950,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:13 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424507408&card[cvc]=704&card[exp_month]=09&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:14 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 161d152a-024b-40e4-a8ee-e4bf94874396
Original-Request: req_7if8915v2yejp5
Request-Id: req_7if8915v2yejp5
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7OEAXIGNKSo5QTO6wGiN",
  "object": "token",
  "card": {
    "id": "card_1LDx7OEAXIGNKSo53DGhmyIg",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "7408",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017954,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411222847&card[cvc]=658&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:18 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 56b91d9e-46c7-4a53-87c5-2d397cc14a89
Original-Request: req_qorozv0j74WYdW
Request-Id: req_qorozv0j74WYdW
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7SEAXIGNKSo5zlNZnwS3",
  "object": "token",
  "card": {
    "id": "card_1LDx7REAXIGNKSo5K8gv683M",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "2847",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017958,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:21 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433761004&card[cvc]=167&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:22 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: dbb3dde7-01c7-48d3-8075-b418ed2fc305
Original-Request: req_GlrEPHZfUkk6uq
Request-Id: req_GlrEPHZfUkk6uq
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7WEAXIGNKSo57aKNeOJs",
  "object": "token",
  "card": {
    "id": "card_1LDx7WEAXIGNKSo53kMrv1Sw",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "1004",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017962,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:25 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425878477&card[cvc]=235&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:26 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ba81e193-649d-4ffd-b803-a8d65c49b83a
Original-Request: req_LYS6VA3kKL5s1s
Request-Id: req_LYS6VA3kKL5s1s
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7aEAXIGNKSo5NPHFDFWb",
  "object": "token",
  "card": {
    "id": "card_1LDx7ZEAXIGNKSo5PwToQrO2",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8477",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017966,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:28 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086416280816&card[cvc]=543&card[exp_month]=10&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:29 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 5095d69b-7431-4b30-9532-f5873121b28c
Original-Request: req_8306DePZeYlquR
Request-Id: req_8306DePZeYlquR
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7dEAXIGNKSo5jhKwsgpW",
  "object": "token",
  "card": {
    "id": "card_1LDx7dEAXIGNKSo5kZDiFVq8",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0816",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017969,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:32 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086406568287&card[cvc]=738&card[exp_month]=12&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:33 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e8d0296d-c012-4551-8277-48485612bda8
Original-Request: req_hrtdQcKaEaHu9n
Request-Id: req_hrtdQcKaEaHu9n
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7hEAXIGNKSo5DFGULrZH",
  "object": "token",
  "card": {
    "id": "card_1LDx7hEAXIGNKSo50LoLOqse",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8287",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017973,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:36 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414561837&card[cvc]=868&card[exp_month]=04&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:37 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6bfeec8a-345c-4cbe-9fbb-99baec75a57b
Original-Request: req_cQk93C1wrCwm2q
Request-Id: req_cQk93C1wrCwm2q
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7lEAXIGNKSo5EtOxyr04",
  "object": "token",
  "card": {
    "id": "card_1LDx7lEAXIGNKSo5AloXZ8xU",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1837",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017977,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:40 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086404171555&card[cvc]=852&card[exp_month]=12&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:41 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 713a8f03-0a52-4eed-9472-b0e2904bd71d
Original-Request: req_W0IVkgEKxzmaVh
Request-Id: req_W0IVkgEKxzmaVh
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7pEAXIGNKSo5d4DCXbVZ",
  "object": "token",
  "card": {
    "id": "card_1LDx7pEAXIGNKSo5PmiIwMsj",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "1555",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017981,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:44 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421360827&card[cvc]=452&card[exp_month]=10&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:45 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: fc5ba9bd-a222-40b6-877b-7cdd76ce0326
Original-Request: req_uOef0pEONWHiXZ
Request-Id: req_uOef0pEONWHiXZ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7tEAXIGNKSo5JIjoLFJC",
  "object": "token",
  "card": {
    "id": "card_1LDx7sEAXIGNKSo5rxCXlFm9",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "0827",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017985,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:48 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425555372&card[cvc]=443&card[exp_month]=10&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:49 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d1b4c79a-b9d8-46b1-995c-95cc9d3866a9
Original-Request: req_YvKnUXtdi8Fnem
Request-Id: req_YvKnUXtdi8Fnem
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx7xEAXIGNKSo5rkQSgsdn",
  "object": "token",
  "card": {
    "id": "card_1LDx7wEAXIGNKSo54LnEYSVs",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5372",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017989,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:52 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433504768&card[cvc]=588&card[exp_month]=11&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:53 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 35b19146-7eca-4616-a816-7192c111b9e8
Original-Request: req_Pyn17Kk9XpPVoE
Request-Id: req_Pyn17Kk9XpPVoE
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx81EAXIGNKSo5hTgM9IMl",
  "object": "token",
  "card": {
    "id": "card_1LDx80EAXIGNKSo5csjmCnMY",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "4768",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017993,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 15:59:56 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424585305&card[cvc]=814&card[exp_month]=02&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 20:59:57 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 3d378b3f-f9e1-4748-842a-0ce18c5ba5d6
Original-Request: req_x8fnmf9pwvN1Yu
Request-Id: req_x8fnmf9pwvN1Yu
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx85EAXIGNKSo5Rb6fCOzC",
  "object": "token",
  "card": {
    "id": "card_1LDx84EAXIGNKSo56xMM4LiH",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5305",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656017997,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:00 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414225474&card[cvc]=152&card[exp_month]=11&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:01 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 631cae51-8a48-4ebb-9be7-d7689b9945a6
Original-Request: req_88fT42B14DKBq3
Request-Id: req_88fT42B14DKBq3
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx89EAXIGNKSo5EHJfQRdd",
  "object": "token",
  "card": {
    "id": "card_1LDx88EAXIGNKSo5WD9mzRrb",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "5474",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018001,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:04 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411231368&card[cvc]=515&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:05 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 75cea76c-c5c9-43e9-a9c9-00897e4e8971
Original-Request: req_LgxK5IRNUpBr4s
Request-Id: req_LgxK5IRNUpBr4s
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8DEAXIGNKSo5eTcWfE0t",
  "object": "token",
  "card": {
    "id": "card_1LDx8CEAXIGNKSo5L4TZy8Um",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1368",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018005,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:08 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420220758&card[cvc]=504&card[exp_month]=12&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:09 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b883dfd4-e239-4850-8e22-e1b12cff3135
Original-Request: req_4JYwQ4Ak8hXPVS
Request-Id: req_4JYwQ4Ak8hXPVS
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8HEAXIGNKSo5leJNdvLZ",
  "object": "token",
  "card": {
    "id": "card_1LDx8HEAXIGNKSo5JaZWpkBZ",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "0758",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018009,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:12 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434838637&card[cvc]=608&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:13 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6e67fd06-faa3-4b2a-b1cb-a5661bc365e7
Original-Request: req_9hKRjQT6d0wbjc
Request-Id: req_9hKRjQT6d0wbjc
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8LEAXIGNKSo5xl0AgJov",
  "object": "token",
  "card": {
    "id": "card_1LDx8LEAXIGNKSo5qZkpzqpJ",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8637",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018013,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:16 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434757258&card[cvc]=367&card[exp_month]=06&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:17 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d3b51cb8-6c4a-4ab5-8b7a-de2ee32e4e59
Original-Request: req_9AfEx8fOrrgmIi
Request-Id: req_9AfEx8fOrrgmIi
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8PEAXIGNKSo5zcxpMc6W",
  "object": "token",
  "card": {
    "id": "card_1LDx8PEAXIGNKSo5jhXACtqz",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "7258",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018017,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:20 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425187572&card[cvc]=875&card[exp_month]=02&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:21 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d68c7867-f403-4560-b9eb-c2eb63cb23f9
Original-Request: req_UycP9tzcRLRHKw
Request-Id: req_UycP9tzcRLRHKw
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8TEAXIGNKSo5gQDnEYlD",
  "object": "token",
  "card": {
    "id": "card_1LDx8TEAXIGNKSo527JIRQmC",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "7572",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018021,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:25 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430181081&card[cvc]=687&card[exp_month]=12&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:26 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7c682edc-0687-420a-9bf5-2563cfab2bd0
Original-Request: req_hrWNTnw7RYNeSS
Request-Id: req_hrWNTnw7RYNeSS
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8YEAXIGNKSo5bxnIAzlt",
  "object": "token",
  "card": {
    "id": "card_1LDx8XEAXIGNKSo5OHJ35KIz",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1081",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018026,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427745203&card[cvc]=734&card[exp_month]=03&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:30 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2010063f-d322-4aa8-b7ba-c6d98bfe6ef2
Original-Request: req_z7uLaynn1HVGEb
Request-Id: req_z7uLaynn1HVGEb
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8cEAXIGNKSo5udEheTs6",
  "object": "token",
  "card": {
    "id": "card_1LDx8cEAXIGNKSo5gbIuuWZc",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "5203",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018030,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:33 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414131045&card[cvc]=235&card[exp_month]=05&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:34 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c89d2041-fa57-435a-ad69-600b0c4a8429
Original-Request: req_pnjOMP7iuT3ivH
Request-Id: req_pnjOMP7iuT3ivH
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8gEAXIGNKSo5MSeErPmg",
  "object": "token",
  "card": {
    "id": "card_1LDx8gEAXIGNKSo5RqYfXsis",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1045",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018034,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:38 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086408146462&card[cvc]=704&card[exp_month]=09&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:39 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 965c0e86-7147-4877-b2fe-9c0408e6df6b
Original-Request: req_UUbcmfvGBO2v8A
Request-Id: req_UUbcmfvGBO2v8A
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8lEAXIGNKSo53PJg6cDA",
  "object": "token",
  "card": {
    "id": "card_1LDx8kEAXIGNKSo5KN5RFaVN",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6462",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018039,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:42 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426185278&card[cvc]=170&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:43 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 1a6b8c5f-5434-4d8c-bf45-dad02c960c10
Original-Request: req_cBw0t6cE5Ua8Gu
Request-Id: req_cBw0t6cE5Ua8Gu
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8pEAXIGNKSo5lxsWATO6",
  "object": "token",
  "card": {
    "id": "card_1LDx8pEAXIGNKSo5gpOse4Id",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5278",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018043,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:46 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424607034&card[cvc]=663&card[exp_month]=10&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:48 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 863919ad-461a-49a8-a063-bce9ecc1e339
Original-Request: req_iNhTjkGcHCvh5V
Request-Id: req_iNhTjkGcHCvh5V
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8tEAXIGNKSo5t1k1GJnd",
  "object": "token",
  "card": {
    "id": "card_1LDx8tEAXIGNKSo5IF0tkBlp",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "7034",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018047,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:51 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425404720&card[cvc]=874&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:52 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2ad6a305-8e86-4fe8-89a4-2036d36ccd71
Original-Request: req_fSzLgxmZgP9c7B
Request-Id: req_fSzLgxmZgP9c7B
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx8yEAXIGNKSo5gBCxBJg7",
  "object": "token",
  "card": {
    "id": "card_1LDx8yEAXIGNKSo5b8ohHPJM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "4720",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018052,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:00:55 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414346767&card[cvc]=123&card[exp_month]=10&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:00:57 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 27e31efd-f9e6-49a6-9ce6-b5398ff181de
Original-Request: req_ncmsn5RmZ4XjZ8
Request-Id: req_ncmsn5RmZ4XjZ8
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx92EAXIGNKSo5MfxOVLAR",
  "object": "token",
  "card": {
    "id": "card_1LDx92EAXIGNKSo5LFpi6jp8",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "6767",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018056,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:00 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430353227&card[cvc]=568&card[exp_month]=12&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:01 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 72b554d8-5341-40c2-8aed-8606bbb7a054
Original-Request: req_2Qfq8eOfGRhCsv
Request-Id: req_2Qfq8eOfGRhCsv
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx97EAXIGNKSo5s1tGJMTa",
  "object": "token",
  "card": {
    "id": "card_1LDx97EAXIGNKSo5JYqmZ6FM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "3227",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018061,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:04 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412618407&card[cvc]=416&card[exp_month]=02&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:06 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 1b7b5829-9289-4289-a30a-c26ade0726ac
Original-Request: req_pXsypJmAZVyEDp
Request-Id: req_pXsypJmAZVyEDp
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9CEAXIGNKSo5l9Y3IdNM",
  "object": "token",
  "card": {
    "id": "card_1LDx9BEAXIGNKSo5ZwqHLm0t",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "8407",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018066,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:09 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428484067&card[cvc]=328&card[exp_month]=08&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:10 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a075e4b2-7d78-468b-86bd-fe9dd9d27ebd
Original-Request: req_Pj2ru2BWXlT1rH
Request-Id: req_Pj2ru2BWXlT1rH
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9GEAXIGNKSo5b1IGTF4D",
  "object": "token",
  "card": {
    "id": "card_1LDx9GEAXIGNKSo5ITHx9u4U",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "4067",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018070,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:14 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427476858&card[cvc]=152&card[exp_month]=11&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:15 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2f80d1f5-67f0-4af3-b43c-406c7ec12124
Original-Request: req_qy0vXvg5xjnlbB
Request-Id: req_qy0vXvg5xjnlbB
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9LEAXIGNKSo5gHJ3drT6",
  "object": "token",
  "card": {
    "id": "card_1LDx9LEAXIGNKSo5VfWRuNZv",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "6858",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018075,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:18 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086410832042&card[cvc]=862&card[exp_month]=02&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:20 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 5da3cb59-db5f-447e-a856-847d52b4f293
Original-Request: req_2YCdfl9cbgkqho
Request-Id: req_2YCdfl9cbgkqho
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9QEAXIGNKSo5cYejXzpW",
  "object": "token",
  "card": {
    "id": "card_1LDx9PEAXIGNKSo53dieHOuS",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "2042",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018080,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:23 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086406232751&card[cvc]=756&card[exp_month]=01&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:24 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 1fa7dad1-01cc-4731-ab18-ecc988415642
Original-Request: req_6TQyPepUD3PbYt
Request-Id: req_6TQyPepUD3PbYt
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9UEAXIGNKSo5ZwkLa5eO",
  "object": "token",
  "card": {
    "id": "card_1LDx9UEAXIGNKSo5D8Tm5k25",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2751",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018084,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427083811&card[cvc]=186&card[exp_month]=03&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:30 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 32c014e3-c4e6-4c8f-8bee-1d4a7b2ee27d
Original-Request: req_V3lxk9N3pK9ijK
Request-Id: req_V3lxk9N3pK9ijK
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9aEAXIGNKSo5XiSq1OJC",
  "object": "token",
  "card": {
    "id": "card_1LDx9ZEAXIGNKSo5SLvIyYAO",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3811",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018090,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:33 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415670561&card[cvc]=812&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:35 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 22c5d906-08c6-4def-b565-6a0846d5224c
Original-Request: req_H0PvH5AhBjPquL
Request-Id: req_H0PvH5AhBjPquL
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9fEAXIGNKSo5WJkqT7tC",
  "object": "token",
  "card": {
    "id": "card_1LDx9eEAXIGNKSo5cDKaREkT",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "0561",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018095,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:38 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086407435361&card[cvc]=502&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:39 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 8b5a10a9-2636-403b-83f0-39d212f3a8c1
Original-Request: req_zZAK4ySpWo4srK
Request-Id: req_zZAK4ySpWo4srK
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9jEAXIGNKSo50T72cpho",
  "object": "token",
  "card": {
    "id": "card_1LDx9jEAXIGNKSo5jcSMhSJ7",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5361",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018099,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:43 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430165423&card[cvc]=380&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:44 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6c57cece-da52-4573-b93e-7a5a09f55c27
Original-Request: req_fITV524EFDb4L0
Request-Id: req_fITV524EFDb4L0
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9oEAXIGNKSo5VOmVgPin",
  "object": "token",
  "card": {
    "id": "card_1LDx9oEAXIGNKSo5782MjNqa",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5423",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018104,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:48 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428223085&card[cvc]=056&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:49 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ba56ab67-3aad-4f49-bb03-fbda69bd74d1
Original-Request: req_2pY6iqlf0RCqz4
Request-Id: req_2pY6iqlf0RCqz4
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9tEAXIGNKSo5xxU9Wj1I",
  "object": "token",
  "card": {
    "id": "card_1LDx9tEAXIGNKSo5KyuFO33c",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "3085",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018109,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:53 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425602042&card[cvc]=405&card[exp_month]=12&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:54 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 397882fd-5875-4276-b3ea-28e974f96c03
Original-Request: req_b87SW32qmKZzxe
Request-Id: req_b87SW32qmKZzxe
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDx9yEAXIGNKSo5E3gpAxw1",
  "object": "token",
  "card": {
    "id": "card_1LDx9yEAXIGNKSo5mNmIHjnt",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2042",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018114,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:01:58 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432883460&card[cvc]=342&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:01:59 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 47dd84b4-029a-4226-bb3f-85cbe05e6066
Original-Request: req_ctx1A6dGEenHXw
Request-Id: req_ctx1A6dGEenHXw
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxA3EAXIGNKSo5G449z8xl",
  "object": "token",
  "card": {
    "id": "card_1LDxA3EAXIGNKSo5wuPPU9EI",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "3460",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018119,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:03 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434205241&card[cvc]=022&card[exp_month]=03&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:04 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ca8ef14a-7ea1-4dd6-8ad5-b37547e653c4
Original-Request: req_ELkDIPuHYm9Kiq
Request-Id: req_ELkDIPuHYm9Kiq
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxA8EAXIGNKSo5kBNjHYW9",
  "object": "token",
  "card": {
    "id": "card_1LDxA8EAXIGNKSo5dZX2zgni",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "5241",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018124,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:08 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086425044245&card[cvc]=676&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:09 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f321c19e-fbed-40d3-b42c-f4a05b2e921c
Original-Request: req_4QxBB2rY6ZYAcq
Request-Id: req_4QxBB2rY6ZYAcq
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxADEAXIGNKSo5uMYeNplv",
  "object": "token",
  "card": {
    "id": "card_1LDxADEAXIGNKSo5d4m4dTZp",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "4245",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018129,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:13 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414685230&card[cvc]=646&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:14 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 27d352b3-c7a9-4fee-94ab-fd250d81c2eb
Original-Request: req_Bra7WsmCCsQSfQ
Request-Id: req_Bra7WsmCCsQSfQ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAIEAXIGNKSo5jBBJaZi3",
  "object": "token",
  "card": {
    "id": "card_1LDxAIEAXIGNKSo59jCqhfId",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5230",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018134,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:19 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428085583&card[cvc]=287&card[exp_month]=03&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:20 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7853f374-6f41-4f54-81c6-ba431656dc45
Original-Request: req_YO3Sn7gAeQyPUX
Request-Id: req_YO3Sn7gAeQyPUX
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAOEAXIGNKSo5ZbmwPEB7",
  "object": "token",
  "card": {
    "id": "card_1LDxAOEAXIGNKSo50bYtNSpf",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5583",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018140,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:24 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415564640&card[cvc]=151&card[exp_month]=08&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:25 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9dd86764-e192-4f35-90ca-004a6768e6fb
Original-Request: req_PP42HE45iJwsk5
Request-Id: req_PP42HE45iJwsk5
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxATEAXIGNKSo5Bd1GxzBT",
  "object": "token",
  "card": {
    "id": "card_1LDxATEAXIGNKSo5R5EMJcXl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "4640",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018145,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412740870&card[cvc]=658&card[exp_month]=05&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:31 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 3e10f74b-6e75-4fc6-8dff-3eb3bfb359c0
Original-Request: req_qHeOb4QSjcbfN9
Request-Id: req_qHeOb4QSjcbfN9
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAZEAXIGNKSo5j5wsp3Fv",
  "object": "token",
  "card": {
    "id": "card_1LDxAYEAXIGNKSo5VlkgIbV4",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0870",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018151,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:35 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422605808&card[cvc]=721&card[exp_month]=01&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:36 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6d9d25c7-4776-4b6b-b6e0-1013aa23b3c2
Original-Request: req_gvLFhV2l0jMVlD
Request-Id: req_gvLFhV2l0jMVlD
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAeEAXIGNKSo5PUFQETlf",
  "object": "token",
  "card": {
    "id": "card_1LDxAdEAXIGNKSo5pdMFXfAZ",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5808",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018156,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:40 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430405126&card[cvc]=420&card[exp_month]=05&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:41 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2978e00c-93c7-4b67-81f9-b856a7759acb
Original-Request: req_clr8BhaR9rvW3g
Request-Id: req_clr8BhaR9rvW3g
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAjEAXIGNKSo5MlJokNTD",
  "object": "token",
  "card": {
    "id": "card_1LDxAjEAXIGNKSo5qmT9lNkz",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5126",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018161,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:45 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428211106&card[cvc]=386&card[exp_month]=04&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:46 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e89233e9-2681-494f-b584-785d1f57ee85
Original-Request: req_BIauo82NfUN25a
Request-Id: req_BIauo82NfUN25a
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAoEAXIGNKSo5j5S5CDi2",
  "object": "token",
  "card": {
    "id": "card_1LDxAoEAXIGNKSo5jAiZOvi6",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1106",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018166,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:51 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421676768&card[cvc]=007&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:52 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 18cfe687-7783-45b1-a28f-1941815d4de8
Original-Request: req_lrLL0AZUKRUCgm
Request-Id: req_lrLL0AZUKRUCgm
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAuEAXIGNKSo5q2oGVVse",
  "object": "token",
  "card": {
    "id": "card_1LDxAtEAXIGNKSo5bUt1D6vL",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "6768",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018172,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:02:56 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086435015086&card[cvc]=041&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:02:57 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 22d714dc-474e-4cfe-8ef5-dbdeb05f9f06
Original-Request: req_mJGHqlndxCsVHa
Request-Id: req_mJGHqlndxCsVHa
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxAzEAXIGNKSo58sdyClX1",
  "object": "token",
  "card": {
    "id": "card_1LDxAzEAXIGNKSo5XuEZdh27",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5086",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018177,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:01 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430135558&card[cvc]=080&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:03 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 8431672a-7820-48bf-89ee-d2355c2985db
Original-Request: req_FOSF0V0L80MMba
Request-Id: req_FOSF0V0L80MMba
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxB4EAXIGNKSo5PT7blcgE",
  "object": "token",
  "card": {
    "id": "card_1LDxB4EAXIGNKSo5CqI0v0Rd",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5558",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018182,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:07 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412506628&card[cvc]=216&card[exp_month]=04&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:08 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7c2b71ef-8b56-47f9-81fe-6a3d25cef867
Original-Request: req_C9smQd8HA9OHOD
Request-Id: req_C9smQd8HA9OHOD
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBAEAXIGNKSo5vY1YWWul",
  "object": "token",
  "card": {
    "id": "card_1LDxBAEAXIGNKSo5K9rsIhr7",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6628",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018188,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:13 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420063646&card[cvc]=303&card[exp_month]=07&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:14 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 66124896-225b-41e2-933c-a1d1ef9af40e
Original-Request: req_A5KwgCaJO0zllb
Request-Id: req_A5KwgCaJO0zllb
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBGEAXIGNKSo5Py0vNYCv",
  "object": "token",
  "card": {
    "id": "card_1LDxBGEAXIGNKSo5bkW4b7cv",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "3646",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018194,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:19 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422245621&card[cvc]=773&card[exp_month]=12&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:20 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e7a0f425-2a28-4757-8a64-24ccfe13bfcd
Original-Request: req_m940L8C98c0ftv
Request-Id: req_m940L8C98c0ftv
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBMEAXIGNKSo5dU2qlNS6",
  "object": "token",
  "card": {
    "id": "card_1LDxBMEAXIGNKSo5HEEdqzpN",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5621",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018200,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:24 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086403738685&card[cvc]=806&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:25 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 46a36582-f007-43f1-ad27-49e56d8969b8
Original-Request: req_f6v8jcIUKlLSmf
Request-Id: req_f6v8jcIUKlLSmf
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBREAXIGNKSo5R5Bht3ZS",
  "object": "token",
  "card": {
    "id": "card_1LDxBREAXIGNKSo50ZL2KmeI",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8685",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018205,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:30 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421106261&card[cvc]=738&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:31 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: efb727e9-72e0-4c0d-b169-c0823efd53c0
Original-Request: req_IkMa41l5srXh6P
Request-Id: req_IkMa41l5srXh6P
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBXEAXIGNKSo5CFOmoxNC",
  "object": "token",
  "card": {
    "id": "card_1LDxBXEAXIGNKSo50APLnbZG",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6261",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018211,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:35 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086417706744&card[cvc]=153&card[exp_month]=02&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:37 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 09791212-eeff-4596-8480-1a54ab006169
Original-Request: req_JlMEfdZsQoEewU
Request-Id: req_JlMEfdZsQoEewU
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBdEAXIGNKSo5nSoJybAl",
  "object": "token",
  "card": {
    "id": "card_1LDxBcEAXIGNKSo5eWXqhVqP",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6744",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018217,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:41 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086418256160&card[cvc]=708&card[exp_month]=04&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:42 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 774fb49f-095c-4322-94aa-185f284b2856
Original-Request: req_ImrvGPpZDBWet6
Request-Id: req_ImrvGPpZDBWet6
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBiEAXIGNKSo5ykkzesPn",
  "object": "token",
  "card": {
    "id": "card_1LDxBiEAXIGNKSo53ZRLuH3B",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6160",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018222,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:47 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421346586&card[cvc]=111&card[exp_month]=06&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:48 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 3975bf41-da6e-437d-a0e7-49e4c3101530
Original-Request: req_t59LSAAhSVkked
Request-Id: req_t59LSAAhSVkked
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBoEAXIGNKSo5hEGTjBkI",
  "object": "token",
  "card": {
    "id": "card_1LDxBoEAXIGNKSo5rcJGx02w",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "6586",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018228,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:53 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086406448886&card[cvc]=515&card[exp_month]=10&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:03:54 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 67b83f88-6114-4d03-967e-b133341ac831
Original-Request: req_C7UHbrPRALi4Dj
Request-Id: req_C7UHbrPRALi4Dj
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxBuEAXIGNKSo5GEkcYONW",
  "object": "token",
  "card": {
    "id": "card_1LDxBtEAXIGNKSo5f361RdYe",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8886",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018234,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:03:58 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414424317&card[cvc]=847&card[exp_month]=08&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:00 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f231d639-9b0a-45cb-a0db-1e14d54235cd
Original-Request: req_lsDcW2dPkshIg0
Request-Id: req_lsDcW2dPkshIg0
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxC0EAXIGNKSo5YRqehY8X",
  "object": "token",
  "card": {
    "id": "card_1LDxBzEAXIGNKSo5mTlb89E1",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4317",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018240,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:04 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420106437&card[cvc]=462&card[exp_month]=01&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:05 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c6ce8f18-d142-4e83-b6c5-212f4be035d6
Original-Request: req_XHdivoW38a8Hst
Request-Id: req_XHdivoW38a8Hst
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxC5EAXIGNKSo5NWQyBo6J",
  "object": "token",
  "card": {
    "id": "card_1LDxC5EAXIGNKSo5cWLJupbc",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6437",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018245,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:11 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086405612672&card[cvc]=784&card[exp_month]=05&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:12 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 97eb0181-c846-47b7-b51c-434ea00694ff
Original-Request: req_5aOi9SXvaXrMzK
Request-Id: req_5aOi9SXvaXrMzK
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCCEAXIGNKSo5i0dtcx2U",
  "object": "token",
  "card": {
    "id": "card_1LDxCCEAXIGNKSo552EzqIyE",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "2672",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018252,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428617542&card[cvc]=035&card[exp_month]=01&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:18 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 95274020-70ad-4003-9462-3a2629ee7e57
Original-Request: req_9TFyjPs8t2hVfP
Request-Id: req_9TFyjPs8t2hVfP
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCIEAXIGNKSo5vdEN26mx",
  "object": "token",
  "card": {
    "id": "card_1LDxCIEAXIGNKSo5oOEG8YfF",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "7542",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018258,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:22 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433356003&card[cvc]=124&card[exp_month]=05&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:23 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: bf1f66e2-2ccb-4c3d-89d6-65aeaa569678
Original-Request: req_0rdKZW7tWf3D9V
Request-Id: req_0rdKZW7tWf3D9V
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCNEAXIGNKSo5FN3wi5bg",
  "object": "token",
  "card": {
    "id": "card_1LDxCNEAXIGNKSo5KEZQrp9S",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6003",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018263,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:28 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421716721&card[cvc]=262&card[exp_month]=11&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:29 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 360796a6-5310-4d83-974a-f7ca0c413d9b
Original-Request: req_J9VXpTBYSKLQe6
Request-Id: req_J9VXpTBYSKLQe6
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCTEAXIGNKSo50mxGw8cG",
  "object": "token",
  "card": {
    "id": "card_1LDxCTEAXIGNKSo50GDJq7PW",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6721",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018269,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:34 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428423883&card[cvc]=711&card[exp_month]=12&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:35 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 549b8f9d-4fbe-49fb-aa2c-d5a473be8f37
Original-Request: req_UjNbtPjDQiywro
Request-Id: req_UjNbtPjDQiywro
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCZEAXIGNKSo5LFdn5JFp",
  "object": "token",
  "card": {
    "id": "card_1LDxCZEAXIGNKSo5Ihcszbzq",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3883",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018275,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:40 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086423501485&card[cvc]=014&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:41 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b94a6a8f-b16b-4638-afd0-cd8a3e7c1ed2
Original-Request: req_6Ahi23Bs4aqXIN
Request-Id: req_6Ahi23Bs4aqXIN
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCfEAXIGNKSo5RVgLWdel",
  "object": "token",
  "card": {
    "id": "card_1LDxCfEAXIGNKSo5AJgvTq2H",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "1485",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018281,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:46 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432607786&card[cvc]=447&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:47 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 895648ab-3db8-4d88-9d55-eed5cd3bf363
Original-Request: req_CZIQU6zYTmBF13
Request-Id: req_CZIQU6zYTmBF13
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxClEAXIGNKSo5pGSr4PkR",
  "object": "token",
  "card": {
    "id": "card_1LDxClEAXIGNKSo5Wf6wzany",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "7786",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018287,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:52 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427647433&card[cvc]=420&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:53 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 38047fd0-5282-40be-80fb-5f59722e9a64
Original-Request: req_1ju6zU064uy39V
Request-Id: req_1ju6zU064uy39V
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCrEAXIGNKSo5Cg0YdMf5",
  "object": "token",
  "card": {
    "id": "card_1LDxCrEAXIGNKSo5K65czZWl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "7433",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018293,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:04:58 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086423176213&card[cvc]=685&card[exp_month]=05&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:04:59 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 148dd86c-1267-4e06-a328-e91b701759b1
Original-Request: req_yxH1CKzjBozpXQ
Request-Id: req_yxH1CKzjBozpXQ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxCxEAXIGNKSo5xrekaGeR",
  "object": "token",
  "card": {
    "id": "card_1LDxCxEAXIGNKSo5wkPDi8c5",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "6213",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018299,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:04 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430810150&card[cvc]=266&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:06 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d394a7e3-ae42-458c-8423-ac3b1ea25349
Original-Request: req_yH5ZUjKJrfcSeD
Request-Id: req_yH5ZUjKJrfcSeD
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxD4EAXIGNKSo5dLkUpP4V",
  "object": "token",
  "card": {
    "id": "card_1LDxD3EAXIGNKSo5rxEJX7Pi",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0150",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018306,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:12 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086414384388&card[cvc]=467&card[exp_month]=01&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:13 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2ec60dd8-b2eb-4731-a366-e67d1460691c
Original-Request: req_kC92kZpzIPx6H8
Request-Id: req_kC92kZpzIPx6H8
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDBEAXIGNKSo5ZYhsFcU2",
  "object": "token",
  "card": {
    "id": "card_1LDxDBEAXIGNKSo5TPMlITif",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4388",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018313,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:18 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086417052420&card[cvc]=605&card[exp_month]=06&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:19 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 49edbfe8-0390-4b19-9ef7-46efa3432127
Original-Request: req_ALce1ioDW88pkc
Request-Id: req_ALce1ioDW88pkc
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDHEAXIGNKSo5xZDtcZyd",
  "object": "token",
  "card": {
    "id": "card_1LDxDHEAXIGNKSo5aAU0D0aY",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "2420",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018319,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:23 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422562884&card[cvc]=137&card[exp_month]=03&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:24 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: fcd7e5f1-096b-4b14-a10b-f00f1d972bbc
Original-Request: req_HaBpjUnFBZ7kqS
Request-Id: req_HaBpjUnFBZ7kqS
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDMEAXIGNKSo5juRulofn",
  "object": "token",
  "card": {
    "id": "card_1LDxDMEAXIGNKSo5CuRN7Rbv",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2884",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018324,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086410126304&card[cvc]=418&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:31 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 43795e40-9210-43e4-a8f0-d56040ce825e
Original-Request: req_Bxur5dqKInJ2jf
Request-Id: req_Bxur5dqKInJ2jf
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDTEAXIGNKSo5Ef6XO6r3",
  "object": "token",
  "card": {
    "id": "card_1LDxDSEAXIGNKSo5rYAcCI87",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6304",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018331,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:36 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426750303&card[cvc]=772&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:37 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7d79ef6c-11a3-4307-91a9-761aa8b036db
Original-Request: req_3pxunyMffMLQ3X
Request-Id: req_3pxunyMffMLQ3X
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDZEAXIGNKSo51RtBBDtd",
  "object": "token",
  "card": {
    "id": "card_1LDxDZEAXIGNKSo5phst8TsN",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0303",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018337,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:42 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086404887218&card[cvc]=352&card[exp_month]=10&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:43 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2fa59908-79cd-495d-9e31-18c77162d92d
Original-Request: req_QsSiC6K3lILEuQ
Request-Id: req_QsSiC6K3lILEuQ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDfEAXIGNKSo5k54jZQsF",
  "object": "token",
  "card": {
    "id": "card_1LDxDfEAXIGNKSo5dt14NNB4",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "7218",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018343,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:47 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086410422323&card[cvc]=444&card[exp_month]=07&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:49 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6be4e2ea-d47b-4d8a-aeef-2805939f1fb8
Original-Request: req_H3rIB64yCruGsT
Request-Id: req_H3rIB64yCruGsT
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDlEAXIGNKSo5WvwaELk8",
  "object": "token",
  "card": {
    "id": "card_1LDxDkEAXIGNKSo5BEU6ebJM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2323",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018349,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:53 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412653040&card[cvc]=707&card[exp_month]=11&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:05:54 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 635e8291-7c9d-4b12-8429-78c8d07a6003
Original-Request: req_Pa4bYrL1SqIQHa
Request-Id: req_Pa4bYrL1SqIQHa
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDqEAXIGNKSo5pjCVx7X4",
  "object": "token",
  "card": {
    "id": "card_1LDxDqEAXIGNKSo5HOo9OHrS",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3040",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018354,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:05:58 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431062561&card[cvc]=647&card[exp_month]=07&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:00 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 37853d4f-3123-495f-b5b7-9b0f4c28037e
Original-Request: req_ewJrzlp8djXXHq
Request-Id: req_ewJrzlp8djXXHq
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxDvEAXIGNKSo5EvtG2LHB",
  "object": "token",
  "card": {
    "id": "card_1LDxDvEAXIGNKSo5epTesiDn",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "2561",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018359,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:04 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415580653&card[cvc]=218&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:05 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 4932aea7-f7d3-4c4a-8179-0dfa38ae4cf3
Original-Request: req_J0ZMEnUlcH70wS
Request-Id: req_J0ZMEnUlcH70wS
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxE1EAXIGNKSo53m6PSRhd",
  "object": "token",
  "card": {
    "id": "card_1LDxE1EAXIGNKSo58oZCaqxd",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0653",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018365,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:10 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086408766582&card[cvc]=413&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:11 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c4396717-ee9a-4fdd-b5a2-7070832dbafa
Original-Request: req_unu19TqNjs8myd
Request-Id: req_unu19TqNjs8myd
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxE7EAXIGNKSo5PfPTB8rF",
  "object": "token",
  "card": {
    "id": "card_1LDxE7EAXIGNKSo5YkSI2BuX",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "6582",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018371,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:16 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086418556262&card[cvc]=581&card[exp_month]=10&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:17 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 4f48352a-65be-40b6-82ce-4f217bb48dd9
Original-Request: req_AMK1HnYdmCv6sR
Request-Id: req_AMK1HnYdmCv6sR
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEDEAXIGNKSo5kP7McBtJ",
  "object": "token",
  "card": {
    "id": "card_1LDxEDEAXIGNKSo5WOzl5Tn5",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "6262",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018377,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:21 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427211016&card[cvc]=206&card[exp_month]=02&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:22 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 63bf60fe-8ce2-48c0-bbe8-3f963ba73871
Original-Request: req_7FwlydjSZlvge7
Request-Id: req_7FwlydjSZlvge7
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEIEAXIGNKSo5N1vAJmaD",
  "object": "token",
  "card": {
    "id": "card_1LDxEIEAXIGNKSo5zHyQkRi9",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "1016",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018382,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:26 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428581367&card[cvc]=881&card[exp_month]=04&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:28 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d89736f3-7cab-4af7-8b85-f9af38f09730
Original-Request: req_gl3L5clURH1flK
Request-Id: req_gl3L5clURH1flK
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEOEAXIGNKSo5rmuRLOuP",
  "object": "token",
  "card": {
    "id": "card_1LDxENEAXIGNKSo5TYPOdYKb",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1367",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018388,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:32 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086430270447&card[cvc]=846&card[exp_month]=02&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:33 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 914241c4-211c-4fb4-abd7-d3c8847931f5
Original-Request: req_8A0hTMZPlnAmfX
Request-Id: req_8A0hTMZPlnAmfX
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxETEAXIGNKSo5jjy1bXfG",
  "object": "token",
  "card": {
    "id": "card_1LDxETEAXIGNKSo5ooLYTeeO",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0447",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018393,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:38 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427632872&card[cvc]=040&card[exp_month]=05&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:39 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 15bbca5e-4369-4a66-90ea-3f275b055130
Original-Request: req_5EytY08JepgyNX
Request-Id: req_5EytY08JepgyNX
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEZEAXIGNKSo5DFJLcw6M",
  "object": "token",
  "card": {
    "id": "card_1LDxEZEAXIGNKSo5FXRzHcxZ",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2872",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018399,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:43 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411350366&card[cvc]=751&card[exp_month]=06&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:44 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c55b5861-63c7-4f71-9315-701f9ac60e7c
Original-Request: req_FgmDjExpm3ynmI
Request-Id: req_FgmDjExpm3ynmI
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEeEAXIGNKSo5o2FlprAv",
  "object": "token",
  "card": {
    "id": "card_1LDxEeEAXIGNKSo5BC5wOnqv",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0366",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018404,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:49 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433035441&card[cvc]=603&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:50 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 4e271db1-5a33-445e-808c-cc19678d7851
Original-Request: req_3vhzKpqFMHd7u7
Request-Id: req_3vhzKpqFMHd7u7
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEkEAXIGNKSo5VSCPTgDD",
  "object": "token",
  "card": {
    "id": "card_1LDxEkEAXIGNKSo5EMwNvX6I",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5441",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018410,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:06:54 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086405888157&card[cvc]=336&card[exp_month]=10&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:06:56 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2403f1d4-23d2-444c-9e7c-bfbea8d75d6f
Original-Request: req_zq2p9mYwrOwjN3
Request-Id: req_zq2p9mYwrOwjN3
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEqEAXIGNKSo5dFxAOhmz",
  "object": "token",
  "card": {
    "id": "card_1LDxEpEAXIGNKSo5xlGUr0SR",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "8157",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018416,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:00 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415386077&card[cvc]=025&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:01 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b5bb9b18-e23e-4614-8d73-5214680473b7
Original-Request: req_zy2uB4SX4OWU3h
Request-Id: req_zy2uB4SX4OWU3h
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxEvEAXIGNKSo5b29A8tFT",
  "object": "token",
  "card": {
    "id": "card_1LDxEvEAXIGNKSo5CFHX9vpg",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6077",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018421,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:07 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434312716&card[cvc]=220&card[exp_month]=10&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:08 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b9966c78-9aeb-44d9-b39f-a962ed991110
Original-Request: req_6Jq1ORsI1vzbOf
Request-Id: req_6Jq1ORsI1vzbOf
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxF2EAXIGNKSo5JYKnEhhR",
  "object": "token",
  "card": {
    "id": "card_1LDxF2EAXIGNKSo5exXx5IBd",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "2716",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018428,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:12 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434426011&card[cvc]=263&card[exp_month]=05&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:14 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0d229b87-cca3-4848-84c8-cdbd799ac84e
Original-Request: req_4AY0YkXRr6SFg6
Request-Id: req_4AY0YkXRr6SFg6
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxF8EAXIGNKSo5lXeXChDT",
  "object": "token",
  "card": {
    "id": "card_1LDxF8EAXIGNKSo5k8Ykbunk",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6011",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018434,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:18 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415821602&card[cvc]=808&card[exp_month]=04&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:20 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ca1095ca-1739-4ec1-b0aa-a569a942ab82
Original-Request: req_W8pr7JXdeHawMs
Request-Id: req_W8pr7JXdeHawMs
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFEEAXIGNKSo572kCsqSl",
  "object": "token",
  "card": {
    "id": "card_1LDxFDEAXIGNKSo5tIw7CmVj",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "1602",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018440,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:24 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432264331&card[cvc]=640&card[exp_month]=01&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:25 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f49cf070-299a-4147-b295-b51d0152d1e7
Original-Request: req_Ue3Q7aKxFQsQXZ
Request-Id: req_Ue3Q7aKxFQsQXZ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFJEAXIGNKSo51N7SXEgh",
  "object": "token",
  "card": {
    "id": "card_1LDxFJEAXIGNKSo5EV49bqCm",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4331",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018445,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:30 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086405808148&card[cvc]=438&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:31 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9fcc5e3d-2a38-4fc9-8fd0-e54340f5fabe
Original-Request: req_ovb31ISflY2g9z
Request-Id: req_ovb31ISflY2g9z
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFPEAXIGNKSo5pydKtUBk",
  "object": "token",
  "card": {
    "id": "card_1LDxFPEAXIGNKSo5WotILqR5",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8148",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018451,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:36 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426038873&card[cvc]=873&card[exp_month]=03&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:37 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0d20b712-09ba-4a01-9672-5123b8a33b08
Original-Request: req_21T79ICUgMoG4Y
Request-Id: req_21T79ICUgMoG4Y
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFVEAXIGNKSo5vPjxAFsg",
  "object": "token",
  "card": {
    "id": "card_1LDxFVEAXIGNKSo57UzdKjNm",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8873",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018457,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:42 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086417200631&card[cvc]=151&card[exp_month]=05&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:43 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: d215c751-2285-4c9d-9925-a7a04c72f0fe
Original-Request: req_heXd5JB0rB9pT9
Request-Id: req_heXd5JB0rB9pT9
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFbEAXIGNKSo5ehr48zhE",
  "object": "token",
  "card": {
    "id": "card_1LDxFbEAXIGNKSo5kecLjswg",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0631",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018463,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:49 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086418347670&card[cvc]=532&card[exp_month]=12&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:50 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9bf052e5-cbdf-48ae-9608-7f2bc8f90084
Original-Request: req_0Vf90Jw8Bd16C8
Request-Id: req_0Vf90Jw8Bd16C8
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFiEAXIGNKSo5sRRgBGKp",
  "object": "token",
  "card": {
    "id": "card_1LDxFiEAXIGNKSo58nAfwVsl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "7670",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018470,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:07:54 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424010460&card[cvc]=207&card[exp_month]=03&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:07:56 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 97766cf3-d04a-4e56-a36d-a393e9276d9e
Original-Request: req_Wgs8SOgFuQA52G
Request-Id: req_Wgs8SOgFuQA52G
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFoEAXIGNKSo5t1COMaBQ",
  "object": "token",
  "card": {
    "id": "card_1LDxFoEAXIGNKSo5e2kDfrip",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0460",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018476,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:00 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086408847002&card[cvc]=121&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:02 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e7da43d1-0f56-4b43-8877-4daf52760a95
Original-Request: req_ZIBPhLAqdh9vLE
Request-Id: req_ZIBPhLAqdh9vLE
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxFuEAXIGNKSo5Vf1nyzSz",
  "object": "token",
  "card": {
    "id": "card_1LDxFuEAXIGNKSo5GEw1G77I",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "7002",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018482,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:08 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086410432173&card[cvc]=637&card[exp_month]=08&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:09 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: cc051127-f817-4436-8f6d-4f87264e9092
Original-Request: req_TsxYc6VIzNjPb3
Request-Id: req_TsxYc6VIzNjPb3
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxG1EAXIGNKSo5hSWQwrk6",
  "object": "token",
  "card": {
    "id": "card_1LDxG1EAXIGNKSo5hWLzr2PV",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2173",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018489,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:14 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086405272287&card[cvc]=223&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:15 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0d064060-ac3f-48c5-9bc4-023b209372e7
Original-Request: req_qlR3FSCOQOz5d7
Request-Id: req_qlR3FSCOQOz5d7
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxG7EAXIGNKSo5tb4qIJEd",
  "object": "token",
  "card": {
    "id": "card_1LDxG7EAXIGNKSo5fQs1QXSp",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2287",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018495,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:20 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420863680&card[cvc]=420&card[exp_month]=09&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:21 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 03148bdb-5f3f-4065-ba7e-01438e08010a
Original-Request: req_uRLk3fYc4ChxzN
Request-Id: req_uRLk3fYc4ChxzN
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGDEAXIGNKSo5xjprZArr",
  "object": "token",
  "card": {
    "id": "card_1LDxGDEAXIGNKSo5BBf5xnAe",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3680",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018501,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:26 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086423038330&card[cvc]=305&card[exp_month]=02&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:27 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f4806c4a-9aca-457f-bc0a-fa774d98cc9e
Original-Request: req_NzDXovNKuYMHQS
Request-Id: req_NzDXovNKuYMHQS
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGJEAXIGNKSo5yMgbdwAs",
  "object": "token",
  "card": {
    "id": "card_1LDxGJEAXIGNKSo5Vy1OzbxE",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "8330",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018507,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:32 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411508443&card[cvc]=408&card[exp_month]=11&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:33 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2b8c71fa-96b7-4d5c-b0cb-c7cf575b38b3
Original-Request: req_M9BVR4HbJGpWb3
Request-Id: req_M9BVR4HbJGpWb3
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGPEAXIGNKSo5pNMIH6Nf",
  "object": "token",
  "card": {
    "id": "card_1LDxGPEAXIGNKSo5SLjk2V75",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8443",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018513,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:38 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086410522262&card[cvc]=568&card[exp_month]=03&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:39 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 4a207036-a3e4-4da5-ad16-75dace55755a
Original-Request: req_ahuQKfhgeHyXhR
Request-Id: req_ahuQKfhgeHyXhR
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGVEAXIGNKSo5H54t1Uin",
  "object": "token",
  "card": {
    "id": "card_1LDxGVEAXIGNKSo5LaNXXixM",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2262",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018519,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:44 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421851668&card[cvc]=204&card[exp_month]=07&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:45 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ceda0d82-8f39-446d-ac49-a3d272670097
Original-Request: req_VSKEeBCtEqz39E
Request-Id: req_VSKEeBCtEqz39E
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGbEAXIGNKSo5SPaBnult",
  "object": "token",
  "card": {
    "id": "card_1LDxGbEAXIGNKSo5qoUofrjS",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "1668",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018525,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:50 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421007212&card[cvc]=716&card[exp_month]=07&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:52 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 6c05d085-5aab-4c02-8fe7-93ec86bcf599
Original-Request: req_uePw9ARmac7yQA
Request-Id: req_uePw9ARmac7yQA
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGiEAXIGNKSo5CbOGWQ9X",
  "object": "token",
  "card": {
    "id": "card_1LDxGhEAXIGNKSo5WzJgKBmF",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "7212",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018532,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:08:56 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086411208713&card[cvc]=855&card[exp_month]=02&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:08:58 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b29284f7-5c39-4977-bbaf-528e2c89d280
Original-Request: req_bHmFGv8IjiNG0u
Request-Id: req_bHmFGv8IjiNG0u
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGoEAXIGNKSo5c2Nb7wRj",
  "object": "token",
  "card": {
    "id": "card_1LDxGnEAXIGNKSo5nQ9ruURp",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8713",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018538,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:02 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086404116121&card[cvc]=186&card[exp_month]=02&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:04 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: aca914e8-d9a0-4e0d-9389-4a7a9d044e32
Original-Request: req_pTD2jgNpB9qODa
Request-Id: req_pTD2jgNpB9qODa
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxGuEAXIGNKSo5n89rDHHR",
  "object": "token",
  "card": {
    "id": "card_1LDxGuEAXIGNKSo5JAOkhyna",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "6121",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018544,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:10 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427084413&card[cvc]=828&card[exp_month]=10&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:11 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 58f9825d-e605-4b06-8ea7-cadded1df46d
Original-Request: req_Ez31YApsGtZTlE
Request-Id: req_Ez31YApsGtZTlE
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxH1EAXIGNKSo5nbPMY1jS",
  "object": "token",
  "card": {
    "id": "card_1LDxH1EAXIGNKSo5x2QjqGoC",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4413",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018551,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:16 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086418807640&card[cvc]=853&card[exp_month]=04&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:18 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f449514d-5fd2-416b-95ea-53186e588bee
Original-Request: req_LyKFmTxu0cit3O
Request-Id: req_LyKFmTxu0cit3O
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxH8EAXIGNKSo5raAqdu9q",
  "object": "token",
  "card": {
    "id": "card_1LDxH7EAXIGNKSo51ijpEieK",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "7640",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018558,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:22 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086428718431&card[cvc]=462&card[exp_month]=06&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:24 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 5ae3d557-96ef-453c-a52c-f3bd5af702b7
Original-Request: req_Cnb6L4IbQUyjIJ
Request-Id: req_Cnb6L4IbQUyjIJ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHEEAXIGNKSo54bOd1vhI",
  "object": "token",
  "card": {
    "id": "card_1LDxHEEAXIGNKSo5rZ72PrQi",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "8431",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018564,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:29 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434176632&card[cvc]=456&card[exp_month]=02&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:30 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2ee7ea29-0201-4a0e-81bb-e3fa77fd4ffb
Original-Request: req_2Z4QdRn79Epl9O
Request-Id: req_2Z4QdRn79Epl9O
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHKEAXIGNKSo5v65R2NSI",
  "object": "token",
  "card": {
    "id": "card_1LDxHKEAXIGNKSo5tUmRO88v",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "6632",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018570,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:35 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422165076&card[cvc]=562&card[exp_month]=12&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:37 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: c45d0aba-af7f-4731-b3bf-057bfcaf5c0a
Original-Request: req_OhfS9lAgE9J3Jg
Request-Id: req_OhfS9lAgE9J3Jg
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHQEAXIGNKSo5v6FiQJBu",
  "object": "token",
  "card": {
    "id": "card_1LDxHQEAXIGNKSo5W0Dp0J44",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5076",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018576,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:41 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086402622641&card[cvc]=424&card[exp_month]=03&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:43 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a870f4f8-388d-4b7c-87e1-c663f1a387c9
Original-Request: req_cuD4EJvQGC8CH9
Request-Id: req_cuD4EJvQGC8CH9
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHXEAXIGNKSo5lsH3aOwk",
  "object": "token",
  "card": {
    "id": "card_1LDxHXEAXIGNKSo5b8okUMsp",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "2641",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018583,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:48 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086434385050&card[cvc]=856&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:50 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 68442d87-4aa0-4710-ac86-f50064a8ac00
Original-Request: req_Cu5L9uOxFXNQbs
Request-Id: req_Cu5L9uOxFXNQbs
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHdEAXIGNKSo5CuW6C3El",
  "object": "token",
  "card": {
    "id": "card_1LDxHdEAXIGNKSo5bJmtYnv6",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5050",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018589,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:09:55 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086407800507&card[cvc]=250&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:09:57 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: a6103b5d-5f6f-445b-b9a1-a4627270cebd
Original-Request: req_yXUKWy2vtWUI7R
Request-Id: req_yXUKWy2vtWUI7R
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHlEAXIGNKSo5gq7yDTso",
  "object": "token",
  "card": {
    "id": "card_1LDxHlEAXIGNKSo5J3il2aTx",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "0507",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018597,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:02 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427113006&card[cvc]=304&card[exp_month]=12&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:04 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2b134920-1234-4d53-ae01-cee57b63869d
Original-Request: req_g3LQRQRnTfdxKC
Request-Id: req_g3LQRQRnTfdxKC
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHrEAXIGNKSo5LaPOhMfq",
  "object": "token",
  "card": {
    "id": "card_1LDxHrEAXIGNKSo5WL5lJZQC",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 12,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "3006",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018603,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:10 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086407885557&card[cvc]=304&card[exp_month]=07&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:11 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: dee49e60-2498-45ae-b520-a632602cb981
Original-Request: req_JVpDMEUAyCjAsk
Request-Id: req_JVpDMEUAyCjAsk
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxHzEAXIGNKSo5xQaX8TLM",
  "object": "token",
  "card": {
    "id": "card_1LDxHzEAXIGNKSo5UKn8dIHk",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "5557",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018611,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427264205&card[cvc]=678&card[exp_month]=03&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:19 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: dd26e867-b90f-4286-ac60-fde8b48e485d
Original-Request: req_REdecD8sN6OfVu
Request-Id: req_REdecD8sN6OfVu
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxI7EAXIGNKSo5AQQ5kZqR",
  "object": "token",
  "card": {
    "id": "card_1LDxI7EAXIGNKSo59zJ2qEg9",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "4205",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018619,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:24 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412510877&card[cvc]=423&card[exp_month]=02&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:25 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: f329262f-c5d3-42b0-bfb8-9982921bd47c
Original-Request: req_HYpBCock3axTAh
Request-Id: req_HYpBCock3axTAh
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIDEAXIGNKSo5h6HGvvjN",
  "object": "token",
  "card": {
    "id": "card_1LDxIDEAXIGNKSo5D2gqQTpF",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0877",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018625,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:31 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086412288318&card[cvc]=816&card[exp_month]=01&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:32 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 2fe445df-9174-48df-bb94-9093e58ccdae
Original-Request: req_fwu8Y5ejefmDZa
Request-Id: req_fwu8Y5ejefmDZa
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIKEAXIGNKSo5HUYP6WSd",
  "object": "token",
  "card": {
    "id": "card_1LDxIKEAXIGNKSo5ruuuwbIj",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "8318",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018632,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:37 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086431563451&card[cvc]=577&card[exp_month]=05&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:39 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 96d0b3b8-55e1-4e7a-ab5f-775c743a2c0d
Original-Request: req_olVjPLRoqOTQ5F
Request-Id: req_olVjPLRoqOTQ5F
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIREAXIGNKSo5oROewVNO",
  "object": "token",
  "card": {
    "id": "card_1LDxIQEAXIGNKSo5jJLjz8E7",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3451",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018639,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:44 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086416554475&card[cvc]=353&card[exp_month]=07&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:45 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e6488df6-9f2e-4377-96af-aac2364d728c
Original-Request: req_Zjr2QVo8L4x3Ty
Request-Id: req_Zjr2QVo8L4x3Ty
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIXEAXIGNKSo5Xn3nl0xR",
  "object": "token",
  "card": {
    "id": "card_1LDxIXEAXIGNKSo58BoomJW8",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "4475",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018645,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:50 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086418674016&card[cvc]=446&card[exp_month]=06&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:52 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b7cd1cc6-0f88-4b4f-b075-eabcf7c99f13
Original-Request: req_cSSVzQ42J3fGcW
Request-Id: req_cSSVzQ42J3fGcW
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIeEAXIGNKSo5tywXCaQ1",
  "object": "token",
  "card": {
    "id": "card_1LDxIdEAXIGNKSo5JYhGqs4c",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "4016",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018652,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:10:57 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086424608750&card[cvc]=241&card[exp_month]=07&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:10:59 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 41301867-c566-4f5c-b681-4051814c6ab0
Original-Request: req_b6g1bcEdkXKvD0
Request-Id: req_b6g1bcEdkXKvD0
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIkEAXIGNKSo5clm5anZJ",
  "object": "token",
  "card": {
    "id": "card_1LDxIkEAXIGNKSo5DJGxSx6w",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "8750",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018658,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:04 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433315801&card[cvc]=845&card[exp_month]=01&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:05 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 9430aff0-f064-40e9-a415-ca34984a4760
Original-Request: req_EoPlROrkbmYHPO
Request-Id: req_EoPlROrkbmYHPO
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIrEAXIGNKSo5XIetpr67",
  "object": "token",
  "card": {
    "id": "card_1LDxIrEAXIGNKSo59ktpT5Tl",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5801",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018665,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:10 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432441053&card[cvc]=477&card[exp_month]=06&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:12 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: da77e789-5436-4426-956d-2776380d29a0
Original-Request: req_DQuwjrvgYZWEWu
Request-Id: req_DQuwjrvgYZWEWu
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxIyEAXIGNKSo5AihJpSJo",
  "object": "token",
  "card": {
    "id": "card_1LDxIxEAXIGNKSo5TJkVZxtd",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 6,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "1053",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018672,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:17 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427470315&card[cvc]=786&card[exp_month]=03&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:19 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 25b37dda-98a8-472d-94b3-7c1603446a00
Original-Request: req_4cH4vzTUkqRqCT
Request-Id: req_4cH4vzTUkqRqCT
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJ4EAXIGNKSo5gWLfP5tH",
  "object": "token",
  "card": {
    "id": "card_1LDxJ4EAXIGNKSo5d3GXLRe6",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "0315",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018678,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:26 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086423271188&card[cvc]=316&card[exp_month]=09&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:28 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: ca58663b-e8ad-4f12-9d92-6a520e8d510c
Original-Request: req_lp3mbkrRewNRUh
Request-Id: req_lp3mbkrRewNRUh
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJEEAXIGNKSo5SedilOVN",
  "object": "token",
  "card": {
    "id": "card_1LDxJEEAXIGNKSo5eq67WtJL",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "1188",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018688,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:33 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086420684060&card[cvc]=550&card[exp_month]=11&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:35 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 050efbc0-1b04-410e-9ec6-2f1b0c63d6ea
Original-Request: req_9WY8Rnni79Blik
Request-Id: req_9WY8Rnni79Blik
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJLEAXIGNKSo5w1HYwxGH",
  "object": "token",
  "card": {
    "id": "card_1LDxJKEAXIGNKSo5BlmD1rmI",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "4060",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018695,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:40 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086427257167&card[cvc]=870&card[exp_month]=02&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:42 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 1a036286-39b6-435c-8134-2fa3f5e2806c
Original-Request: req_HXEkwQ4GhncRib
Request-Id: req_HXEkwQ4GhncRib
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJREAXIGNKSo5qtIOUxeQ",
  "object": "token",
  "card": {
    "id": "card_1LDxJREAXIGNKSo5DTfesyri",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 2,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "7167",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018701,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:47 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086416174480&card[cvc]=416&card[exp_month]=11&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:48 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: e5c23f36-da1e-4807-8418-d23fb108518b
Original-Request: req_m3FBoLoTzKDNf4
Request-Id: req_m3FBoLoTzKDNf4
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJYEAXIGNKSo5pZ1J7wZm",
  "object": "token",
  "card": {
    "id": "card_1LDxJYEAXIGNKSo5UQXq5Du1",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 11,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "4480",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018708,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:11:54 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086415125871&card[cvc]=031&card[exp_month]=09&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:11:55 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: b39239a4-a889-4c11-927e-2f23d8673ed8
Original-Request: req_YIiqURRX9YF9kA
Request-Id: req_YIiqURRX9YF9kA
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJfEAXIGNKSo5ExZrhU0S",
  "object": "token",
  "card": {
    "id": "card_1LDxJfEAXIGNKSo563LUO8vj",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "5871",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018715,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:01 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426445441&card[cvc]=251&card[exp_month]=01&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:02 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 0df38823-1224-4f29-bc8b-a74d122e81c7
Original-Request: req_qibJKhZ2b0mdUQ
Request-Id: req_qibJKhZ2b0mdUQ
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJmEAXIGNKSo5oiXx0Slk",
  "object": "token",
  "card": {
    "id": "card_1LDxJmEAXIGNKSo5g21kDUwX",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 1,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "5441",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018722,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:07 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422543413&card[cvc]=774&card[exp_month]=05&card[exp_year]=24&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:09 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 8aa8c8d3-4f37-4514-a1ad-e9dca66c569a
Original-Request: req_n6s5MrkUyOuYJU
Request-Id: req_n6s5MrkUyOuYJU
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxJtEAXIGNKSo5xGMREUBN",
  "object": "token",
  "card": {
    "id": "card_1LDxJtEAXIGNKSo5RpgMw0Yn",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 5,
    "exp_year": 2024,
    "funding": "debit",
    "last4": "3413",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018729,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:14 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086426833828&card[cvc]=243&card[exp_month]=10&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1507</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:16 GMT
Content-Type: application/json
Content-Length: 730
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 874b27c4-8d96-4c04-b5c6-7b1ffe6bc02c
Original-Request: req_MU8Q75ju8kFeYH
Request-Id: req_MU8Q75ju8kFeYH
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxK0EAXIGNKSo54J4wh5IG",
  "object": "token",
  "card": {
    "id": "card_1LDxK0EAXIGNKSo5bByt7A93",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 10,
    "exp_year": 2026,
    "funding": "debit",
    "last4": "3828",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018736,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:21 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086421572520&card[cvc]=123&card[exp_month]=03&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:23 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 26e0dda1-7621-4203-b4e5-d6434e1458fa
Original-Request: req_YlTNQIlvwSlVJG
Request-Id: req_YlTNQIlvwSlVJG
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxK7EAXIGNKSo5EEeOPxC6",
  "object": "token",
  "card": {
    "id": "card_1LDxK7EAXIGNKSo5QbEfBbWg",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 3,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "2520",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018743,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:28 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086422545384&card[cvc]=357&card[exp_month]=09&card[exp_year]=25&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:30 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 395a7569-12a3-455f-837b-5eb0fa45ecc3
Original-Request: req_rVThf7bnpvimdn
Request-Id: req_rVThf7bnpvimdn
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxKEEAXIGNKSo5ibSWiVv6",
  "object": "token",
  "card": {
    "id": "card_1LDxKEEAXIGNKSo55x0kH6Av",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2025,
    "funding": "debit",
    "last4": "5384",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018750,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:37 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086432431435&card[cvc]=318&card[exp_month]=07&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:38 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 814fbbba-437f-4e04-8c7a-3dde5407f87b
Original-Request: req_8iHB7iY06Yl1Dr
Request-Id: req_8iHB7iY06Yl1Dr
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxKMEAXIGNKSo5IWfUdzi9",
  "object": "token",
  "card": {
    "id": "card_1LDxKMEAXIGNKSo5lkfC6mP4",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 7,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "1435",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018758,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:44 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433804176&card[cvc]=532&card[exp_month]=09&card[exp_year]=27&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:45 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 40cb2d57-ad06-42d5-9cae-ba99d5e8cbf4
Original-Request: req_IEDgEO8ys697iL
Request-Id: req_IEDgEO8ys697iL
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxKTEAXIGNKSo5M595Z8lB",
  "object": "token",
  "card": {
    "id": "card_1LDxKTEAXIGNKSo5QavDA7l9",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "4176",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018765,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:51 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

""","""]=Juan+Ramirez&card[number]=4381086433814746&card[cvc]=786&card[exp_month]=06&card[exp_year]=26&guid=2b444e4a-872a-445c-a5cb-cdef9afd1fb84754d9&muid=6f1488f6-04c7-498d-817d-d36707f712753055bf&sid=b40644ef-ebb7-4a99-8620-306223ff0448916be5&payment_user_agent=stripe.js%2Fa928bb833%3B+stripe-js-v3%2Fa928bb833&time_on_page=546090&key=pk_live_v7Tuoi3xVdLrLVeTRWbqGi1D&pasted_fields=number]]></request>
    <status>200</status>
    <responselength>1506</responselength>
    <mimetype>JSON</mimetype>
    <response base64="false"><![CDATA[HTTP/2 200 OK
Server: nginx
Date: Thu, 23 Jun 2022 21:12:52 GMT
Content-Type: application/json
Content-Length: 729
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, HEAD, OPTIONS, DELETE
Access-Control-Allow-Origin: https://js.stripe.com
Access-Control-Expose-Headers: Request-Id, Stripe-Manage-Version, X-Stripe-External-Auth-Required, X-Stripe-Privileged-Session-Required
Access-Control-Max-Age: 300
Cache-Control: no-cache, no-store
Idempotency-Key: 7852c5a5-3809-47b8-89f2-ec631a1642dd
Original-Request: req_pOcDii6VIcfWjz
Request-Id: req_pOcDii6VIcfWjz
Stripe-Should-Retry: false
Stripe-Version: 2020-08-27
Timing-Allow-Origin: https://js.stripe.com
Strict-Transport-Security: max-age=31556926; includeSubDomains; preload

{
  "id": "tok_1LDxKaEAXIGNKSo575E6S9Qa",
  "object": "token",
  "card": {
    "id": "card_1LDxKaEAXIGNKSo5tZCmTXUv",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "EC",
    "cvc_check": "unchecked",
    "dynamic_last4": null,
    "exp_month": 9,
    "exp_year": 2027,
    "funding": "debit",
    "last4": "4176",
    "name": "Juan Ramirez",
    "tokenization_method": null
  },
  "client_ip": "157.100.91.25",
  "created": 1656018765,
  "livemode": true,
  "type": "card",
  "used": false
}
]]></response>
    <comment></comment>
  </item>
  <item>
    <time>Thu Jun 23 16:12:51 ECT 2022</time>
    <url><![CDATA[https://api.stripe.com/v1/tokens]]></url>
    <host ip="34.202.153.183">api.stripe.com</host>
    <port>443</port>
    <protocol>https</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/v1/tokens]]></path>
    <extension>null</extension>
    <request base64="false"><![CDATA[POST /v1/tokens HTTP/2
Host: api.stripe.com
Content-Length: 394
Sec-Ch-Ua: "-Not.A/Brand";v="8", "Chromium";v="102"
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://js.stripe.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://js.stripe.com/
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9
Connection: close

"""]

  
if __name__ == "__main__":
  run()