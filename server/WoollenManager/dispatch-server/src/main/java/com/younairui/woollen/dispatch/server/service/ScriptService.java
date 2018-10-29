package com.younairui.woollen.dispatch.server.service;

import org.springframework.core.io.FileSystemResource;

/**
 * Created by 刘悦之 on 2018/10/27.
 */
public interface ScriptService {
    public FileSystemResource getScriptFile(String scriptFileName,String scriptVersion);
}
