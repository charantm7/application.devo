from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title="Interactive line graph", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend_label="Line", line_width=2)
p.annular_wedge(x=5, y=5, inner_radius=0.2, outer_radius=0.4, start_angle=45, end_angle=135, line_color="red", fill_color="red")
show(p)
