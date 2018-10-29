package com.younairui.woollen.dispatch.server.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

/**
 * Created by 刘悦之 on 2018/6/27.
 */
@Component
@ConfigurationProperties(prefix = "woollen.script")
public class ScriptProperties {

    String path;

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
}
