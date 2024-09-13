from selenium import webdriver


def test_scores_service(url):
    try:
        dr = webdriver.Chrome()
        dr.get(url)
        score = dr.find_element(by="id", value="score").text
        if 1 <= int(score) <= 1000:
            return True
        else:
            return False
    except AssertionError as e:
        return False


def main():
    url = "http://127.0.0.1:5000"
    if test_scores_service(url):
        print("cool")
        return 0
    else:
        print("damn")
        return -1


main()

