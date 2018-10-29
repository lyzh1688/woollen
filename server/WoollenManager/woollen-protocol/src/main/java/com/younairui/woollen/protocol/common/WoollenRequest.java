package com.younairui.woollen.protocol.common;

/**
 * Created by 刘悦之 on 2018/10/24.
 */
public class WoollenRequest extends Header {

    private String appName;
    private String appVersion;
    private String clientType;

    public String getAppName() {
        return appName;
    }

    public void setAppName(String appName) {
        this.appName = appName;
    }

    public String getAppVersion() {
        return appVersion;
    }

    public void setAppVersion(String appVersion) {
        this.appVersion = appVersion;
    }

    public String getClientType() {
        return clientType;
    }

    public void setClientType(String clientType) {
        this.clientType = clientType;
    }
}
