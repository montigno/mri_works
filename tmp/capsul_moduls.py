from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="maps_img" type="string" doc=""/>
	<input name="display_mode" type="string" doc=""/>
	<input name="title" type="string" doc=""/>
	<input name="colorbar" type="bool" doc=""/>
</process>
''')
def Plot_prob_atlas(maps_img, display_mode, title, colorbar):
	listInputs=dict(zip(('maps_img', 'display_mode', 'title', 'colorbar'),(maps_img, display_mode, title, colorbar)))
	return cs.Plot_prob_atlas(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="atlas_name" type="string" doc=""/>
	<return name="atlas_filename" type="string" doc=""/>
</process>
''')
def fetch_atlas_smith_2009(atlas_name,):
	listInputs=dict(zip(('atlas_name',),(atlas_name,)))
	return cs.fetch_atlas_smith_2009(**listInputs).atlas_filename()

