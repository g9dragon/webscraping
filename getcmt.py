def clcmt(jsstr,bs,scmtd):
    bcmt=jsstr.find('"content"',bs)
    if bcmt<bs:
        return scmtd
    ecmt=jsstr.find('",',bcmt,len(jsstr))
    cmt=str(jsstr[bcmt+11:ecmt]).strip().split('<br/>')
    acmtd=scmtd
    acmtd.append(str(cmt))
    clcmt(jsstr,ecmt,acmtd)
    return scmtd

