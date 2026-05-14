# Chicago Building Violations API Doc

There are 3 endpoints for this Chicago Building Violations API.
- GET violations by address
- GET scofflaw since violation date
- POST comment for address

The sample server address is http://127.0.0.1:8000/

### Endpoints ###
<b>GET</b>
<br>http://127.0.0.1:8000/property/\<address\>/
<br>
<br> Retrieve the violations of a single address. And whether there are any scofflaws for this address. Replace {host} with your server domain.

The response will return a json with:
- last_violation_date (date)
- total_violations (int)
- scofflaw (boolean)
- list of violations (array of json objects)

<br><b>Example Request:</b>
<br>http://127.0.0.1:8000/property/6117%20S%20RACINE%20AVE/

<b>Response:</b>
<br>Status: HTTP 200 OK
```json
{
    "last_violation_date": "2024-07-30",
    "total_violations": 4,
    "scofflaw": true,
    "violations": [
        {
            "id": "7196127",
            "violation_date": "2024-07-30",
            "violation_code": "CN190029",
            "violation_status": "OPEN",
            "violation_description": "ARRANGE FOR REINSPECTION REGAR",
            "violation_inspector_comments": "INTERIOR OF BUILDING , NO ENTRY NO RESPONSE . UNABLE TO VERIFY SMOKE OR CARBON MONOXIDE ALARMS.",
            "address": "6117 S RACINE AVE",
            "scofflaw_record_id": "14-M1-402101-2021-09-01",
            "scofflaw_defendant_owner": "WESLEY REALTY GROUP, INCORPORATED"
        },
        {
            "id": "7116435",
            "violation_date": "2024-02-03",
            "violation_code": "PL160017",
            "violation_status": "OPEN",
            "violation_description": "REMV OBSTR FROM DRAINAGE SYSTM",
            "violation_inspector_comments": "NaN",
            "address": "6117 S RACINE AVE",
            "scofflaw_record_id": "14-M1-402101-2021-09-01",
            "scofflaw_defendant_owner": "WESLEY REALTY GROUP, INCORPORATED"
        },
        {
            "id": "7116436",
            "violation_date": "2024-02-03",
            "violation_code": "CN061034",
            "violation_status": "OPEN",
            "violation_description": "FLAKY INTERIOR PAINT",
            "violation_inspector_comments": "NaN",
            "address": "6117 S RACINE AVE",
            "scofflaw_record_id": "14-M1-402101-2021-09-01",
            "scofflaw_defendant_owner": "WESLEY REALTY GROUP, INCORPORATED"
        },
        {
            "id": "7116437",
            "violation_date": "2024-02-03",
            "violation_code": "CN190019",
            "violation_status": "OPEN",
            "violation_description": "ARRANGE PREMISE INSPECTION",
            "violation_inspector_comments": "ARRANGE FOR INSPECTION AFTER REPAIRS - (312) 743-0413",
            "address": "6117 S RACINE AVE",
            "scofflaw_record_id": "14-M1-402101-2021-09-01",
            "scofflaw_defendant_owner": "WESLEY REALTY GROUP, INCORPORATED"
        }
    ]
}
```

<b>GET</b>
<br>http://127.0.0.1:8000/property/scofflaws/violations
<br>
<br> Retrieve a list of scofflaw addresses. Filter for address with violations since date with the optional parameter 'since='. Otherwise all scofflaw addresses are returned

<b>Option parameters:</b>
<br>since=\<yyyy-mm-dd>

<b>Example GET Request:</b>
<br>http://127.0.0.1:8000/property/scofflaws/violations?since=2024-01-01

<b>Response:</b>
<br>Status: HTTP 200 OK
```json
[
    "7548 S BLACKSTONE AVE",
    "4755 S SHIELDS AVE",
    "730 W 66TH PL",
    "9628 S FOREST AVE",
    "4624 S ELLIS AVE",
    "8034 S ELLIS AVE",
    "7507 S CARPENTER ST",
    "4230 S MICHIGAN AVE",
    "8118 S DREXEL AVE",
    "1554 E 65TH ST",
    "1115 E 81ST ST",
    "4527 S WABASH AVE",
    "5342 N KEDZIE AVE"
]
```

<b>POST</b>
<br>http://127.0.0.1:8000/property/\<address\>/comments/
<br>
<br> Add comment to address.
<br>Post to this comments endpoint of the property address with a json body that includes 'author' and 'comment' keys. Both author and comment are required.

Example POST Request:
```bash
curl -X POST "http://127.0.0.1:8000/property/6117%20S%20RACINE%20AVE/comments/" \
  -H "Content-Type: application/json" \
  -d '{"author":"jun","comment":"sample comment"}'
```

<b>Response:</b>
<br>Status: HTTP 201 CREATED
```json
{
    "status": "success",
    "message": "Comment added successfully.",
    "comment_added": [
        "6117 S RACINE AVE",
        "sample comment"
    ]
}
```
