import allure
from selene import browser

def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )

def add_logs(browser):
    try:
        # Проверяем, поддерживает ли драйвер логи
        if hasattr(browser.driver, 'get_log'):
            logs = browser.driver.get_log('browser')
            log_text = "".join(f'{log["level"]}: {log["message"]}\n' for log in logs)
            allure.attach(
                log_text,
                name="Browser Logs",
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                "Browser logs not supported for this driver",
                name="Browser Logs Info",
                attachment_type=allure.attachment_type.TEXT
            )
    except Exception as e:
        allure.attach(
            f"Error getting browser logs: {str(e)}",
            name="Browser Logs Error",
            attachment_type=allure.attachment_type.TEXT
        )

def add_html(browser):
    html = browser.driver.page_source
    allure.attach(
        body=html,
        name='page_source',
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )

def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(
        body=html,
        name='video_' + browser.driver.session_id,
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )