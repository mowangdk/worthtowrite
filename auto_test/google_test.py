from splinter import Browser

browser = Browser('chrome')

if __name__ == '__main__':
    url = 'http://www.google.com'
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web application')
    # Find and click the 'search' button

    button = browser.find_by_name('btnK')
    element = browser.find_element_

    # interact with element
    button.click()

    if browser.is_text_present('splinter.readthedocs.io'):
        print 'yes, the official website was found'

    else:
        print "no it wasn't found .... we need to improve our seo techniques"
