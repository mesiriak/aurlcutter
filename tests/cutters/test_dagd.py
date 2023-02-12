async def test_dagd_cut(dagd_cutter, client, test_url):
    manual_response = await client.get(dagd_cutter.api_url, params={"url": test_url})

    response = await dagd_cutter.cut(test_url)

    assert manual_response.text.strip() == response
