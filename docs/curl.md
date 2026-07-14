```bash
curl 'https://api.ucloud.cn/?Action=CreateTiDBClusterService' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,zh;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -b 'is_dark_theme_on=0; channel_key=; HMACCOUNT=B0D81EF5E54D38F9; U_CHANNEL_ID=1; das_session=524c857e-644a-4e59-ad4e-5a3c784e4ca7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219882a5e0183f-0bd5046cb892a58-17525636-3686400-19882a5e01920e4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk4ODJhNWUwMTgzZi0wYmQ1MDQ2Y2I4OTJhNTgtMTc1MjU2MzYtMzY4NjQwMC0xOTg4MmE1ZTAxOTIwZTQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219882a5e0183f-0bd5046cb892a58-17525636-3686400-19882a5e01920e4%22%7D; c_project_1126973789_qq_com={%22ProjectId%22:%22org-ykr2u5%22%2C%22ProjectName%22:%22Default%22}; c_region_1126973789_qq_com={%22Region%22:%22cn-bj2%22%2C%22Zone%22:%22cn-bj2-02%22}; U_LANG=zh_CN; CN_lang=zh_CN; _lang=CN; Feedback_ID=98; SurveyCookieTest=1; c_project_umongodb_sub_ucloud_cn={%22ProjectId%22:%22org-ut0f1o%22%2C%22ProjectName%22:%22Default%22}; c_region_umongodb_sub_ucloud_cn={%22Region%22:%22ge-fra%22%2C%22Zone%22:%22ge-fra-01%22}; _gcl_au=1.1.1161941614.1778038221; _ga=GA1.1.45779041.1779692097; _ga_DZSMXQ3P9N=GS2.1.s1781230890$o2$g0$t1781231075$j60$l0$h0; U_USER_EMAIL=walter.chen%40ucloud.cn; U_COMPANY_ID=6025; U_USER_ID=150675020; U_MANAGER=devopsforcrm%40ucloud.cn; Hm_lvt_413fdc5943040809ed0703eabd01f173=1782790895; _gcl_aw=GCL.1782876670.CjwKCAjw0o3SBhBVEiwAh28-jXxzynYrXCt60jHG2OtzkNL44Wvie0voThklUQP8NysKo5miFGuQdhoCCe4QAvD_BwE; _gcl_gs=2.1.k1$i1782876659$u208098198; Hm_lpvt_413fdc5943040809ed0703eabd01f173=1783651413; _uetsid=b80078c07b4811f1961ce9451e8b3df4|5k8k61|2|g7m|0|2381; _uetvid=fc4d9b203f8811f1a2ab8127141c7360|wy9yld|1783651450858|4|1|bat.bing.com/p/conversions/c/i; U_JWT_TOKEN=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODM2OTQ2NzIsImp0aSI6IjFnY29rQkRBd0dXRm9xS0FOT2tZd2EiLCJpYXQiOjE3ODM2NTE0NzIsInN1YiI6InVjczppYW06OjYwMjU6dXNlci8xNTA2NzUwMjAiLCJzZCI6e319.py0uY3oo0TOacS9LbJQLw5PbNghGHn2mOmx6rW6F3vDyOcPMmN_xVUehA19CSTGRw1edwownH5-TdXUEbgJ8zQ; U_CSRF_TOKEN=7bd53172ab21c5666764b6f31eee037c; c_project_walter_chen_ucloud_cn={%22ProjectId%22:%22org-mcimio%22%2C%22ProjectName%22:%22UDB%E4%B8%B4%E6%97%B6%E6%B5%8B%E8%AF%95(%E5%B0%8F%E4%BA%8E7%E5%A4%A9)%22}; c_region_walter_chen_ucloud_cn={%22Region%22:%22cn-bj2%22%2C%22Zone%22:%22$%22}; c_last_region_walter_chen_ucloud_cn={%22Region%22:%22cn-bj2%22%2C%22Zone%22:%22cn-bj2-02%22}' \
  -H 'Origin: https://console.ucloud.cn' \
  -H 'Referer: https://console.ucloud.cn/tidb/create' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'U-CSRF-Token: 7bd53172ab21c5666764b6f31eee037c' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'x-api-lang: zh_CN' \
  --data-raw '{"ProjectId":"org-mcimio","Zone":"cn-bj2-03","Region":"cn-bj2","Name":"TiDB-chen","Password":"abcd1234","VPCId":"uvnet-eevc2cxx","SubnetId":"subnet-ps2ywaqk","NewCollationEnabled":1,"NewCollationsEnabledONFirstBootstrap":1,"DTType":"10","ChargeType":"Month","Quantity":1,"TemplateId":"bb9a1c6a-78e6-11f1-9a61-0242c6122001","DbVersion":"v8.5.6","Labels":[],"NodeConfig.0.ServerType":"Tikv","NodeConfig.0.NodeCount":3,"NodeConfig.0.ConfigId":"tikv_4c_16g","NodeConfig.0.DiskSize":200,"NodeConfig.1.ServerType":"Tidb","NodeConfig.1.NodeCount":2,"NodeConfig.1.ConfigId":"tidb_2c_4g","NodeConfig.1.DiskSize":200,"NodeConfig.2.ServerType":"Pd","NodeConfig.2.NodeCount":3,"NodeConfig.2.ConfigId":"pd_2c_4g","OrderDetail.0.ProductName":"CPU","OrderDetail.1.ProductName":"MEM","OrderDetail.2.ProductName":"DISK","OrderDetail.0.Multiple":22,"OrderDetail.1.Multiple":68,"OrderDetail.2.Multiple":1000,"AlertStrategyIds":[],"Action":"CreateTiDBClusterService","_user":"walter.chen@ucloud.cn","_timestamp":1783677379049}'
```

- response

```json
{
    "Action": "CreateTiDBClusterServiceResponse",
    "RetCode": 0,
    "Message": "",
    "ServiceId": "tidbcluster-1snt2lbdhxr3",
    "Data": {
        "Id": "tidbcluster-1snt2lbdhxr3"
    }
}
```


