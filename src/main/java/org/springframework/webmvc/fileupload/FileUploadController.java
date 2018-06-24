package org.springframework.webmvc.fileupload;

import org.springframework.mvc.extensions.ajax.AjaxUtils;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.multipart.MultipartFile;

@Controller
@RequestMapping("/fileupload")
public class FileUploadController {

	@ModelAttribute
	public void ajaxAttribute(WebRequest request, Model model) {
		model.addAttribute("ajaxRequest", AjaxUtils.isAjaxRequest(request));
	}

	@GetMapping
	public void fileUploadForm() {
	}

	@PostMapping
	public void processUpload(@RequestParam MultipartFile file, Model model) {
		model.addAttribute("message", "File '" + file.getOriginalFilename() + "' uploaded successfully");
	}
	
}
