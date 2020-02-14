import sys
from capsul.api import get_process_instance
from PyQt5.Qt import QApplication


parameter_dict={}        
if len(sys.argv) > 2:
    for user_input in sys.argv[2:]:
        varname = user_input.split("=")[0]
        varvalue = user_input.split("=")[1]
        try:
            varvalue = eval(varvalue)
        except:
            pass
        parameter_dict[varname] = varvalue
        
try:
	xmlpipe = get_process_instance("capsul_pipeline")
	xmlpipe.Atlas_name="sub-prob-2mm"
	xmlpipe.U1_display_mode="ortho"
	xmlpipe.U1_colorbar=True
	if sys.argv[1] == "runPipeline":
		if parameter_dict:
			xmlpipe(**parameter_dict)
		else:
			xmlpipe()
except Exception as e:
	print("error execution pipeline : ",e)

try:
    if sys.argv[1] == 'showInputs':
        for key_s,val_s in xmlpipe.get_inputs().items():
            if 'nodes_activation' not in key_s:
                print(key_s,'= ',val_s)
except:
    pass

try:
    if sys.argv[1] == 'showOutputs':
        for key_s,val_s in xmlpipe.get_outputs().items():
            print(key_s,'= ',val_s)
except:
    pass

try:
    if sys.argv[1] in ['-help','-h'] :
        print("""
        usage:  python3 capsul_main.py runPipeline [attributs=value] (1) 
                python3 capsul_main.py showPipeline                  (2)
                python3 capsul_main.py showInputs                    (3)
                python3 capsul_main.py showOutputs                   (4)

        (1) - run pipeline : - with default values of inputs if no option
                             - with value assigned to certain (or all) inputs
                                    (ex : python3 capsul_main.py executionPipeline X=10.0 Y=[5.6])
        (2) - show pipeline developper view
        (3) - show pipeline inputs with default values
        (4) - show pipeline outputs 
        """)
except:
    pass
        
try:
    if sys.argv[1] == "showPipeline":
        if globals().get('use_gui', True):
            from capsul.qt_gui.widgets import PipelineDevelopperView
            run_qt_loop=False
            if QApplication.instance() is None:
                app=QApplication(sys.argv)
                run_qt_loop=True
            else:
                app = QApplication.instance()
             
            view4 = PipelineDevelopperView(xmlpipe, allow_open_controller=True, show_sub_pipelines=True)
            view4.show()
             
            if run_qt_loop:
                print('close window to gon on ...')
                app.exec_()
except Exception as e:
    print("error show pipeline : ",e)
                    