import wikipedia
def get_page_summary():
    while True:
        title = input("Enter a page title or search phrase (or blank to exit): ")
        if title == "":
            break

        try:
            # Get the page and print the summary
            page = wikipedia.page(title, auto_suggest=False)
            print("Summary of", title, ":\n", page.summary, "\n")
        except wikipedia.DisambiguationError as e:
            print(title, "refers to several pages. Please be more specific.")
            print(e.options)
        except wikipedia.PageError:
            print("Page", title, "does not exist.")
        except Exception as e:
            print("An error occurred: ", e)


if __name__ == '__main__':
    get_page_summary()