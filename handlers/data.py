import re
import json

rgb_keys = ('r', 'g', 'b')
hsl_keys = ('h', 's', 'l')


def parse_colors(soup):
    """ create list with color codes hex, rgb and hsl format
     :param soup: source page
     :returns colors: list of color codes"""
    colors = []

    # get chart element by ID
    chart_element = soup.find('header', {'id': 'flat'})

    # parse all div elements with class 'color-group'
    for color_group in chart_element.findAll('div', class_='color-group'):
        # parse all div with class 'js-color'
        for color_element in chart_element.findAll('div', class_='js-color'):
            # append element to colors
            colors.append({
                'hex': color_element['data-hex'].upper(),
                'rgb': get_color_data(color_element['data-rgb'], rgb_keys),
                'hsl': get_color_data(color_element['data-hsl'], hsl_keys)
            })
    return colors


def get_color_data(string, keys):
    """ function to create dictionary with color codes
    :param string: color codes from source page
    :param keys: hex,rgb or hsl
    :returns : color codes dict"""
    values = get_values_from_string(string)
    return {key: value for key, value in zip(values, keys)}


def get_values_from_string(data):
    """ matches filter type of color codes
    :param data: page source
    :returns: list with color codes values"""
    result = []
    pattern = r'[0-9]+%?'
    matches = re.findall(pattern, data)
    for match in matches:
        result.append(match)
    return result


def write_output(target, data):
    """ creates json file output
     :param target: html source
     :param data: color codes list
     """
    data.append(target)
    with open('output_data.json', 'w') as json_file:
        json_object = json.dumps(data)
        json_file.write(json_object)
