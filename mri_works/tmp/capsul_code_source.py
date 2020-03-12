class div_int_dyn:
    def __init__(self,int1=0,int2=1,**dynamicsInputs):
        self.res = int(int1/int2)
        for di in dynamicsInputs:
            self.res= int(self.res/dynamicsInputs[di])
        
    def division(self:'int'):
        return self.res   


class StringToInt():
    def __init__(self,inString=''):
        from sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ=='int':
            self.outval=val
        else:
            self.outval=None
            
    def outInt(self:'int'):
        return self.outval


class ImageJ_execution():
    def __init__(self,command=''):
        import os
        import subprocess
        from subprocess import Popen
        subprocess.Popen(['ImageJ','-eval',command],shell=False)


class ImageJ_load_Image():
    def __init__(self, file='path'):
        import os
        img_current = os.path.basename(file)
        script = "fileCurrent = " + "\"" + file + "\"" + ";imageCurrent = " + "\"" + img_current + "\";open(fileCurrent);run('Enhance Contrast', 'saturated=0.35');"
        self.cmd = script
   
    def cmd_post(self:'str'):
        return self.cmd


class index_list_str:
    def __init__(self,list_in_str=[''],index=0):
        self.outVal = list_in_str[index]
        
    def out_list_indexed(self:'str'):
        return self.outVal


class askopenfilename():
    def __init__(self,extension='*.*',title='choose your file'):
        import tkinter as tk
        from tkinter import filedialog
        root=tk.Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilename(title=title,filetypes=[('', extension)])
        
    def filePath(self:'path'):
        return self.filename


class Plot_profil():
    def __init__(self, cmd_ant='', coord=[0, 0, 0, 0]):
        coords = tuple(coord)
        txt=','.join(str(x) for x in coords)
        self.cmd = cmd_ant + "\nselectWindow(imageCurrent);makeLine("+txt+");run(\"Plot Profile\");"
        
    def cmd_post(self:'str'):
        return self.cmd


class build_list_int_dyn:
    def __init__(self,int_in=0,**dynamicsInputs):
        self.outList = [int_in]
        for di in dynamicsInputs:
            self.outList.append(dynamicsInputs[di])
        
    def out_list(self:'list_int'):
        return self.outList


class Nifti_rawInfo():

    def __init__(self, nii_image='path',
                        structarr="enumerate(('sizeof_hdr'," + 
                                             "'data_type'," + 
                                             "'db_name'," + 
                                             "'extents'," + 
                                             "'session_error'," + 
                                             "'regular'," + 
                                             "'dim_info'," + 
                                             "'dim'," + 
                                             "'intent_p1'," + 
                                             "'intent_p2'," + 
                                             "'intent_p3'," + 
                                             "'intent_code'," + 
                                             "'datatype'," + 
                                             "'bitpix'," + 
                                             "'slice_start'," + 
                                             "'pixdim'," + 
                                             "'vox_offset'," + 
                                             "'scl_slope'," + 
                                             "'scl_inter'," + 
                                             "'slice_end'," + 
                                             "'slice_code'," + 
                                             "'xyzt_units'," + 
                                             "'cal_max'," + 
                                             "'cal_min'," + 
                                             "'slice_duration'," + 
                                             "'toffset'," + 
                                             "'glmax'," + 
                                             "'glmin'," + 
                                             "'descrip'," + 
                                             "'aux_file'," + 
                                             "'qform_code'," + 
                                             "'sform_code'," + 
                                             "'quatern_b'," + 
                                             "'quatern_c'," + 
                                             "'quatern_d'," + 
                                             "'qoffset_x'," + 
                                             "'qoffset_y'," + 
                                             "'qoffset_z'," + 
                                             "'srow_x'," + 
                                             "'srow_y'," + 
                                             "'srow_z'," + 
                                             "'intent_name'," + 
                                             "'magic'))"):
        import nibabel as nib
        img = nib.load(nii_image)
        hdr = img.header
        
        self.str = hdr.structarr[structarr].tolist()
        
    def out_structarr(self:'list_str'):
        return self.str


