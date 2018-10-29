package com.younairui.woollen.protocol.dispatch;

import com.younairui.woollen.protocol.common.WoollenResponse;

/**
 * Created by 刘悦之 on 2018/10/24.
 */
public class ScriptVersionCheckResponse extends WoollenResponse {

    //是否需要强制升级
    Boolean isExpire;
    //服务端最新版本号
    String latestScriptVersion;

    public Boolean getExpire() {
        return isExpire;
    }

    public void setExpire(Boolean expire) {
        isExpire = expire;
    }

    public String getLatestScriptVersion() {
        return latestScriptVersion;
    }

    public void setLatestScriptVersion(String latestScriptVersion) {
        this.latestScriptVersion = latestScriptVersion;
    }
}
