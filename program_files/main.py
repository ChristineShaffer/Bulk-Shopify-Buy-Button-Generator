import csv
import os


def read_in_products(path):
    try:
        with open(path, "rU") as infile:
            readCSV = csv.reader(infile)
            lines = [line for line in readCSV]
            return lines[1:]
    except IOError:
        print("Error reading in product csv!")


def write_out_buttons(folder, lines):
    try:
        with open(folder + "/outputs/generated-buy-buttons.csv", "w") as outfile:
            for line in lines:
                buy_button = '"' + "<div data-embed_type='product' "
                buy_button += "data-shop='" + line[3].lower() + ".myshopify.com "
                buy_button += "data-product_name='" + line[1] + "' "
                buy_button += "data-product_handle='" + line[0] + "' "
                buy_button += ("data-has_image='false' "
                               "data-display_size='compact' data-redirect_to='cart' data-buy_button_text='Add to cart' "
                               "data-buy_button_out_of_stock_text='Out of Stock' "
                               "data-buy_button_product_unavailable_text='Unavailable' "
                               "data-button_background_color='7fb466' "
                               "data-button_text_color='ffffff' data-product_modal='false' "
                               "data-product_title_color='000000' "
                               "data-next_page_button_text='Next page'>" + '"\n')
                outfile.write(buy_button)
    except IOError:
        print("Error writing out Buy Buttons")


def main():

    # Get input folder
    while True:
        file = input("Enter csv file name (no extension): ")

        if (os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/inputs/" + file + ".csv") and
           (file != ".") and (file != "..") and (file != "") and (file != "/")):
            folder_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/inputs/" + file + ".csv"
            break
    else:
        print("File does not exist, please enter exact name of file")

    # Read in product csv
    product_lines = read_in_products(file_path)

    # Write out buy buttons
    write_out_buttons(folder_path, product_lines)


if __name__ == '__main__':
    main()