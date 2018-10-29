package com.younairui.woollen.protocol.dispatch;

/**
 * Created by 刘悦之 on 2018/10/24.
 */
public class ScriptDownloadRequest {

    String targetScriptName;
    //下载目标版本号
    String targetScriptVersion;


    public String getTargetScriptName() {
        return targetScriptName;
    }

    public void setTargetScriptName(String targetScriptName) {
        this.targetScriptName = targetScriptName;
    }

    public String getTargetScriptVersion() {
        return targetScriptVersion;
    }

    public void setTargetScriptVersion(String targetScriptVersion) {
        this.targetScriptVersion = targetScriptVersion;
    }
}
