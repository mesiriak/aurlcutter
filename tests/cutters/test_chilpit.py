async def test_chilpit_cut(chilpit_cutter, client, test_url):
    manual_response = await client.get(chilpit_cutter.api_url, params={"url": test_url})

    response = await chilpit_cutter.cut(test_url)

    assert manual_response.text.strip() == response
