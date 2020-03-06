from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="in_path" type="string" doc=""/>
	<input name="in_path_0" type="string" doc=""/>
	<input name="in_path_1" type="string" doc=""/>
	<return name="path_list" type="list_file" doc=""/>
</process>
''')
def build_list_path_dyn(in_path, in_path_0, in_path_1):
	listInputs=dict(zip(('in_path', 'in_path_0', 'in_path_1'),(in_path, in_path_0, in_path_1)))
	return cs.build_list_path_dyn(**listInputs).path_list()

@xml_process('''
<process capsul_xml="2.0">
	<input name="in_files" type="list_file" doc=""/>
	<return name="smoothed_files" type="list_file" doc=""/>
</process>
''')
def spm_Smooth(in_files,):
	listInputs=dict(zip(('in_files',),(in_files,)))
	return cs.spm_Smooth(**listInputs).smoothed_files()

