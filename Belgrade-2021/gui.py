from ipywidgets import *


def build_widgets(widgets):
    _w_list = []

    v_layout = Layout(
        display='flex',
        flex_flow='column',
        justify_content='space-between'
    )

    h_layout = Layout(
        display='flex',
        flex_flow='row',
        justify_content='space-between'
    )

    # Country widgets
    lbl_countries = Label(value='Country')
    countries = Combobox(options=[])
    _w_list.append(Box([lbl_countries, countries], layout=v_layout))

    # Subregion widgets
    lbl_unit = Label(value='Area source ID')
    units = Dropdown(options=[])
    _w_list.append(Box([lbl_unit, units], layout=v_layout))

    # Plot type widgets
    lbl_plot = Label(value='Plot type')
    plot_type = Dropdown(
        options=['CSZ only', 'Tecto. only', 'ASZ only', 'Tecto. vs. ASZ',
                 'Tecto. vs. FSZ'])
    _w_list.append(Box([lbl_plot, plot_type], layout=v_layout))

    # Find plot button
    plot_button = Button(description='Plot')
    _w_list.append(Box([plot_button], layout=v_layout))

    return GridBox(_w_list)

