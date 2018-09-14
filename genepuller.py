import urllib.request as ul

#http://www.cbioportal.org/webservice.do?cmd=getCaseLists&cancer_study_id=gbm_tcga
basedict = Dict(
    [
        ('scheme', 'http'),
        ('netloc', 'www.cbioportal.org'),
        ('path', '/webservice.do'),
        ('params', ''),
        ('query', ''),
        ('fragment', '')
    ]
)
cmd_dict = {
    'cancers','getTypesOfCancer',
    'networks','getNetwork',
    'studies','getCancerStudies',
    'genetics','getGeneticProfiles',
    'profiles','getProfileData',
    'caselists','getCaseLists',
    'clinical','getClinicalData',
    'mutations','getMutationData',
}
keystr = ", ".join(cmd_dict.keys())
def qbuilder(key,attr=None):
    if key not in cmd_list.keys():
        estr = "key must be one of ["
        estr+=keystr+']\n'
        estr+= "recieved: %s"
        raise AttributeError(estr%key)
    qstr = 'cmd=%s'%(cmd_dict[key])
    if attr is not None:
        qstr += 
    
