from Page import Helper


def test_search(browser):
    main_page = Helper(browser)
    main_page.go_to_site()
    main_page.main_page_locators()


def test_login(browser):
    main_page = Helper(browser)
    main_page.go_to_site()
    main_page.menu_login_click()
    main_page.signin()
    main_page.account_page_locators()
    