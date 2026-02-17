Installing and Basic Interaction with curl

```
curl --version

# output :

curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.19
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
````

___
Fetching Data from an API:

```
curl https://jsonplaceholder.typicode.com/posts

# output :

{
    "userId": 10,
    "id": 98,
    "title": "laboriosam dolor voluptates",
    "body": "doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores"
  }
```
___

Using Headers and Other Options with curl:

```
curl -I https://jsonplaceholder.typicode.com/posts.

# output :

HTTP/2 404 
date: Tue, 17 Feb 2026 11:28:20 GMT
content-type: application/json; charset=utf-8
content-length: 2
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=NKHFF8PkaR3PhrB0dwqA6REXII7Z6S2iOdbPahAi0pM%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1771327700"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=NKHFF8PkaR3PhrB0dwqA6REXII7Z6S2iOdbPahAi0pM%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1771327700"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1771327712
cf-cache-status: EXPIRED
cf-ray: 9cf4f0cf0b9613d3-MRS
alt-svc: h3=":443"; ma=86400
```

```
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

# output :

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```