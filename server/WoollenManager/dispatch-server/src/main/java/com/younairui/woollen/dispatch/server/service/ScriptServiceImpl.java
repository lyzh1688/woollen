package com.younairui.woollen.dispatch.server.service;

import com.younairui.woollen.dispatch.server.config.ScriptProperties;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.FileSystemResource;
import org.springframework.stereotype.Service;

/**
 * Created by 刘悦之 on 2018/10/27.
 */
@Service
public class ScriptServiceImpl implements ScriptService {

    @Autowired
    ScriptProperties scriptProperties;

    @Override
    public FileSystemResource getScriptFile(String scriptFileName,String scriptVersion) {
        String filePath = scriptProperties.getPath() + scriptVersion;
        FileSystemResource file = new FileSystemResource(filePath);
        return file;
    }
}
