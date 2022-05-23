def print_country_capital_pairs(countries, capitals):
    countries = [country for country in countries.split(', ')]
    capitals = [capital for capital in capitals.split(', ')]

    zipped_country_capitals = zip(countries, capitals)

    return {print(f'{pair[0]} -> {pair[1]}') for pair in zipped_country_capitals}
    

print_country_capital_pairs(input(), input())
