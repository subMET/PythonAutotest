from request import get_other_posts_titles, get_my_posts_descriptions, send_post

def test_step1(authorize, title_in_other_post):
    titles = get_other_posts_titles(authorize)
    assert title_in_other_post in titles

def test_step2(authorize):
    send_post(authorize, "TitleText", "DescriptionText", "ContentText")
    descriptions = get_my_posts_descriptions(authorize)
    assert "DescriptionText" in descriptions