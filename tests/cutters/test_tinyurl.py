async def test_tinyurl_cut(tiny_cutter, client, test_url):
    manual_response = await client.get(tiny_cutter.api_url, params={"url": test_url})

    response = await tiny_cutter.cut(test_url)

    assert manual_response.text == response
