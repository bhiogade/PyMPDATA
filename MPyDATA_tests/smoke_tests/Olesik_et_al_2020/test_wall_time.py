from MPyDATA_examples.Olesik_et_al_2020.setup import Setup, default_nr, default_GC_max
from MPyDATA_examples.Olesik_et_al_2020.coordinates import x_id, x_log_of_pn, x_p2
from MPyDATA_examples.Olesik_et_al_2020.simulation import Simulation
from MPyDATA import Options
from MPyDATA_examples.Olesik_et_al_2020.setup import Setup, default_mixing_ratios_g_kg
from difflib import context_diff
import numpy as np

grid_layout_set = (x_log_of_pn(base=2),)
opt_set = (
    {'n_iters': 1},
    {'n_iters': 2},
    {'n_iters': 2,'infinite_gauge':True},
    {'n_iters': 2, 'infinite_gauge': True, 'flux_corrected_transport': True},
    {'n_iters': 2, 'third_order_terms':True},
    {'n_iters': 3},
    {'n_iters': 3, 'third_order_terms': True, 'infinite_gauge': True, 'flux_corrected_transport': True}
)



def test_wall_time(iters = 3):
    setup = Setup(nr=default_nr, mixing_ratios_g_kg=np.array([2,]))
    table_data = {"opts":[], "values":[]}
    for grid in grid_layout_set:
        norm = [1, ]
        for opts in opt_set:
            i = 0
            minimum_values = []
            while i < iters:
                result = make_data(setup, grid, opts)
                wall_times = result['wall_time']
                min_time = np.nanmin(wall_times)
                minimum_values.append(min_time)
                i+=1
            selected_value = np.min(minimum_values)
            if opts == {'n_iters': 1}:
                norm[0] = selected_value
            table_data["opts"].append(str(opts)+ "(" +grid.__class__.__name__+ ")")
            table_data["values"].append(round(selected_value/norm[0],2))
    make_refdata(table_data, generate=True)


def make_data(setup,grid,opts):
    options = Options(**opts)
    simulation = Simulation(setup=setup, grid_layout=grid, psi_coord=x_id(), opts=options, GC_max=default_GC_max)
    result = {"wall_time": []}
    last_step = 0
    for n_steps in simulation.out_steps:
        steps = n_steps - last_step
        wall_time = simulation.step(steps)
        last_step += steps
        result['wall_time'].append(wall_time)
    return result

def make_refdata(data, generate=False):
    latex_data = r"\hline" + " Variant  & Elapsed Real Time (wrt upwind) " + r"\\ \hline" + "\n"
    for opt, value in zip(data["opts"], data["values"]):
            latex_data += r"\hline" + f" {opt} & {value} " + r"\\ \hline" + "\n"
    latex_start = r"\begin"+ "\n" +"{table}[]" +"\n" +r"\begin"+ "\n"+ "{tabular}"+ "\n" +"{| l | l |}"+ "\n"
    latex_end = "\end \n {tabular} \n \end \n {table}"
    latex_table = latex_start + latex_data + latex_end
    f = open("wall_time_refdata.txt", "w+")
    if generate:
        f.write(latex_table)
    else:
        for line in context_diff(f, latex_table, fromfile='before.py', tofile='after.py'):
            sys.stdout.write(line)
    f.close()





