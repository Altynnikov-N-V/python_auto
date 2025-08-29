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
        # Проверяем, поддерживает ли драйвер логи и есть ли метод get_log
        driver = browser.driver
        if hasattr(driver, 'get_log') and callable(getattr(driver, 'get_log')):
            try:
                logs = driver.get_log('browser')
                log_text = "".join(f'{log["level"]}: {log["message"]}\n' for log in logs)
                allure.attach(
                    log_text,
                    name="Browser Logs",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as log_error:
                # Если get_log есть, но не работает
                allure.attach(
                    f"Error getting browser logs: {str(log_error)}",
                    name="Browser Logs Error",
                    attachment_type=allure.attachment_type.TEXT
                )
        else:
            # Получаем базовую информацию о драйвере
            driver_info = f"Driver: {type(driver).__name__}\n"
            driver_info += f"Capabilities: {getattr(driver, 'capabilities', 'N/A')}\n"

            # Пытаемся получить консольные логи через JavaScript
            try:
                console_logs = driver.execute_script("return window.console && console.logs ? console.logs : [];")
                if console_logs:
                    console_text = "".join(f'{log}\n' for log in console_logs)
                    allure.attach(
                        console_text,
                        name="Console Logs (JS)",
                        attachment_type=allure.attachment_type.TEXT
                    )
            except Exception as js_error:
                console_logs = None

            allure.attach(
                f"Browser logs not supported for this driver\n{driver_info}",
                name="Browser Logs Info",
                attachment_type=allure.attachment_type.TEXT
            )
    except Exception as e:
        allure.attach(
            f"Error in add_logs function: {str(e)}",
            name="Browser Logs Function Error",
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