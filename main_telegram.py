import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


try:
    # Открываем сайт
    driver.get("https://shop.foodsoul.pro/")

    # Нажать самовывоз
    pickup = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[4]/div/div/div/ul/li[2]")))
    pickup.click()
    print('Нажал "Самовывоз"')

    # Нажать первый ТЦ
    shop_cent = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/ul/li[1]")))
    shop_cent.click()
    print('Нажал "ТЦ"')

    # Нажать кнопку аккаунта
    account = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#topBar > div > div > div.topbar__menu > div > div > div.popover__relative > button")))
    account.click()
    print('Нажал "Аккаунт"')

    # Нажать кнопку "telegram"
    telegram = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#topBar > div > div > div.topbar__menu > div > div > div.popover__content > form > "
                          "div.login-ways > div > "
                          "button.button.position-relative.d-inline-flex.align-items-center.overflow-hidden.outline"
                          "-none.cursor-pointer.us-none.button--default.button--large.button--custom.button"
                          "--uppercase.button--expanded > div")))
    telegram.click()
    print('Нажал "Telegram"')

    # Капча
    while True:
        try:
            WebDriverWait(driver, 7).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[4]/div[2]/iframe')))

            input('Встретилась капча, пройдите её, затем нажмите "Enter" ')

            # Нажать кнопку "telegram"
            telegram = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#topBar > div > div > div.topbar__menu > div > div > div.popover__content > form > "
                                  "div.login-ways > div > "
                                  "button.button.position-relative.d-inline-flex.align-items-center.overflow-hidden"
                                  ".outline"
                                  "-none.cursor-pointer.us-none.button--default.button--large.button--custom.button"
                                  "--uppercase.button--expanded")))
            telegram.click()
            print('Нажал "Telegram"')
            break

        except Exception as ex:
            print('Капча не найдена')
            break

    # Нажать кнопку "открыть"
    butt_open = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#topBar > div > div > div.topbar__menu > div > div > div.popover__content > div > a")))
    butt_open.click()
    print('Нажал "Открыть"')

    # Пользователь вручную выполняет авторизацию через telegram
    input("Авторизуйтесь через телеграмм, убедитесь, что вошли в аккаунт, затем нажмите Enter ")

    # Прокрутка страницы к меню ресторана
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#recommendrecommend > div > div:nth-child(1) > div.product__wrapper > div.product-menu > "
                          "div.product-actions > button > div")))
    ActionChains(driver) \
        .scroll_to_element(iframe) \
        .perform()
    print('прокрутил к элементу')

    # Добавление товара в корзину
    product_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#recommendrecommend > div > div:nth-child(1) > div.product__wrapper > div.product-menu > "
                          "div.product-actions > button > div")))
    product_add.click()
    print('кликнул на добавить в корзину')

    # Нажать кнопку корзины
    basket = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#app > div.pe-none.cart-button.container > div > div > div > button")))
    basket.click()
    print('Кликнул на корзину')

    # Выбор элемента корзины
    time.sleep(1)  # Корзина без ожидания не до конца прогружается, по этому использовал time.sleep
    screen = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#app > div.pe-none.cart-button.container > div > div > div.popover__content")))
    screen.screenshot('./image/basket_image.png')
    print('сохранил скриншот корзины')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
