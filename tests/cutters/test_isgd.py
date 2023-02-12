async def test_isgd_cut(isgd_cutter, client, test_url):
    manual_response = await client.get(
        isgd_cutter.api_url, params={"format": "simple", "url": test_url}
    )

    response = await isgd_cutter.cut(test_url)

    assert manual_response.text == response
