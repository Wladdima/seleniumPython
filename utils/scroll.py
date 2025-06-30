def scroll_element_into_view(browser, element):
    browser.execute_script('arguments[0].scrollIntoView();', element)
