package com.younairui.woollen.dispatch.server.endpoint;

import com.younairui.woollen.dispatch.server.service.ScriptService;
import com.younairui.woollen.protocol.dispatch.ScriptDownloadRequest;
import com.younairui.woollen.protocol.dispatch.ScriptVersionCheckRequest;
import com.younairui.woollen.protocol.dispatch.ScriptVersionCheckResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.InputStreamResource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;

/**
 * Created by 刘悦之 on 2018/10/24.
 *
 * 脚本管理接口
 */

@Controller("ScriptManagerEndpoint")
public class ScriptManagerEndpoint {

    @Autowired
    ScriptService scriptService;

    @RequestMapping(value = "/woollen/dispatch/scriptVersionCheck",method = {RequestMethod.POST})
    @ResponseBody
    public ScriptVersionCheckResponse scriptVersionCheck(@RequestBody ScriptVersionCheckRequest request){
        ScriptVersionCheckResponse response = new ScriptVersionCheckResponse();
        response.setExpire(false);
        response.setLatestScriptVersion("1.0.0.1");
        return response;
    }

    @RequestMapping(value = "/woollen/dispatch/scriptDownload",method = RequestMethod.POST)
    public ResponseEntity<InputStreamResource> scriptDownload(@RequestBody ScriptDownloadRequest scriptDownloadRequest) throws IOException {
        FileSystemResource file = this.scriptService.getScriptFile(scriptDownloadRequest.getTargetScriptName(),scriptDownloadRequest.getTargetScriptVersion());
        HttpHeaders headers = new HttpHeaders();
        headers.add("Cache-Control", "napplication.ymlo-cache, no-store, must-revalidate");
        headers.add("Content-Disposition", String.format("attachment; filename=\"%s\"", file.getFilename()));  
        headers.add("Pragma", "no-cache");  
        headers.add("Expires", "0");
        return ResponseEntity
                .ok()
                .headers(headers)
                .contentLength(file.contentLength())
                .contentType(MediaType.parseMediaType("application/octet-stream"))
                .body(new InputStreamResource(file.getInputStream()));
    }
}
