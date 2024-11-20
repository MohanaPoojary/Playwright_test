from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page=browser.new_page()
    #page.goto('https://demo.automationtesting.in/Index.html')

    # cssSelector = id - #, class - ., attribute - taname[attrribute="value"]
   
    # id using
    
    # email_textbox = page.wait_for_selector('#email')
    # email_textbox.type('test@gmail.com')
    
    # login_button = page.wait_for_selector('#enterimg')
    # login_button.click()

    # page.wait_for_timeout(3000)

    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username_textbox = page.wait_for_selector('input[name="username"]')
    username_textbox.type('Admin')

    password_textbox = page.wait_for_selector('input[type="password"]')
    password_textbox.type('admin123')

    submit_button = page.wait_for_selector('button[type="submit"]')
    submit_button.click()

    page.wait_for_timeout(3000)



    

