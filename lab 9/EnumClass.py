class EnumClass:
    metrics = ['npg', 'birth_rate', 'death_rate', 'gdw', 'urbanization']
    metricsNames = ['Natural poplutaion growth', 'Birth rate', 'Death rate', 'General demographic weight', 'Urbanization']
    titles = ['Main dataset', 'Approximation', 'Regression', 'Predictions']
    labels = ['Choose region ', 'Enter year ', 'Draw', 'Metrics', 'Predictions by approximation', 'Predictions by regression:', 'Natural poplutaion growth:', 'Birth rate:', 'Death rate:', 'General demographic weight:', 'Urbanization:']
    errors = ['Region value error', 'Region value shouldn\'t be empty', 'Year value error', 'Wrong value of year', 'Year value error', 'Value of year should be bigger than 2017']
    YEAR = 'year'
    REGION = 'region'
    FILENAME = 'dataset.csv'
    START_YEAR_FOR_APPROXIMATION = 2018
    START_YEAR_FOR_REGRESSION = 1990
    COMBOBOX_STATE = 'readonly'
    A_COEF_INDEX = 0
    B_COEF_INDEX = 1
    C_COEF_INDEX = 2
    D_COEF_INDEX = 3
    INTERPORATION_METHOD = 'cubic'
    WIDTH = 25
    WINDOW_GEOMETRY = '900x300'
    FONT_SIZE = 15
    FONT = 'Times'
    COLUMNS_COUNT = 5
    ROWS_COUNT = 2
    APPROXIMATION_COLOR = 'orangered'
    REGRESSION_COLOR = 'green'
    APPROXIMATION = 'Approximation'
    REGRESSION = 'Regression'
    HEADERS_COLOR = 'lightskyblue'
    WIDGETS_COLOR = 'white'
    RELIEF = 'solid'
    PARAMETR_TEXT_WIDTH = 27
    BUTTON_WIDTH = 12