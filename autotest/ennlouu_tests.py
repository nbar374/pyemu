import os
if not os.path.exists("temp"):
    os.mkdir("temp")


def rosenbrock_2par_setup():
    import pyemu
    os.chdir(os.path.join("ennlouu","rosenbrock_2par"))
    in_file = os.path.join("par.dat")
    tpl_file = in_file+".tpl"
    out_file = os.path.join("obs.dat")
    ins_file = out_file+".ins"
    pst = pyemu.helpers.pst_from_io_files(tpl_file,in_file,ins_file,out_file)
    par = pst.parameter_data
    par.loc[:,"partrans"] = "none"
    par.loc[:,"parval1"] = 2.0
    par.loc[:,"parubnd"] = 7.0
    par.loc[:,"parlbnd"] = -3.0
    obs = pst.observation_data
    obs.loc[:,"obsval"] = 0.0
    obs.loc[:,"weight"] = 1.0
    pst.model_command = ["python rosenbrock_2par.py"]
    pst.control_data.noptmax = 0
    #pst.pestpp_options["sweep_parameter_csv_file"] = os.path.join("sweep_in.csv")
    pst.write(os.path.join("rosenbrock_2par.pst"))

    os.chdir(os.path.join("..",".."))

def rosenbrock_2par_initialize():
    import pyemu
    os.chdir(os.path.join("ennlouu", "rosenbrock_2par"))
    esqp = pyemu.EnsembleSQP(pst="rosenbrock_2par.pst")
    esqp.initialize(num_reals=10)
    os.chdir(os.path.join("..", ".."))

#def rosenbrock_2par_opt_and_draw_setting_invest():
    # function for identifying appropr default values (for simple problem)

if __name__ == "__main__":
	#rosenbrock_2par_setup()
    rosenbrock_2par_initialize()