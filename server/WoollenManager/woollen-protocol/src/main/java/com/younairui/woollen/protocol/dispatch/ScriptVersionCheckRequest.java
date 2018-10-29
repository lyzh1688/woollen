package com.younairui.woollen.protocol.dispatch;

import com.younairui.woollen.protocol.common.WoollenRequest;

/**
 * Created by 刘悦之 on 2018/10/24.
 */
public class ScriptVersionCheckRequest extends WoollenRequest {

    //客户端本地版本号
    String scriptVersion;

    public String getScriptVersion() {
        return scriptVersion;
    }

    public void setScriptVersion(String scriptVersion) {
        this.scriptVersion = scriptVersion;
    }
}
