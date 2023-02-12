import re


async def test_osdb_cut(osdb_cutter, client, test_url):
    
    response_re = re.compile(r"http:\/\/osdb\.link\/.*<", re.IGNORECASE)
    
    manual_response = await client.post(osdb_cutter.api_url, data={"url": test_url})

    response = await osdb_cutter.cut(test_url)

    assert response_re.findall(manual_response.text)[0].strip("<") == response
