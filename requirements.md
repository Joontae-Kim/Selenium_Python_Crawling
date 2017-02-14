<html>
	<body>
		<h4>This document is daily learing note about Seleium crawler with python </h4>
		<p>Under order is this document's default format</p>
		<ol>
			<li> file name</li>
			<li> requirement message</li>
		</ol>
		<hr>
		<ol>
			<li> crawling_script_0214.py</li>
			<li> Setting the Seleium crawler's development environment.</li>
			<ol>
				<li>
					<h3>Install Seleium package.</h3>
					<p> My development environment : MacOS, Python2, Sublime Text2.,<br>
					If you didn't install Python, you have to download setup file under an official site. you can find out proper setup file to your OS.<br>  https://www.python.org/downloads/</p>
				</li>
				<li>
					<h3>Install Seleium package.</h3>
					<cite>Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) also be automated as well.</cite>
					<p>by http://www.seleniumhq.org/</p>
					<p>To install, write <code>pip install selenium</code> In command shell</p>
					<p>If you want to check whether installed or not, write under some code. </p>
					<code>python2</code> <br>
					<code>>>>import selenium</code> <br>
					<code>>>>selenium__version__</code> 
				</li>
				<li>
					<h3>Install Seleium WebDriver.</h3>
					<p>Seleium WebDriver is a bridge between OS and Web Browser. If you want to use Seleium WebDriver, you have to choose a right version both OS and Web Browser.</p>
					<cite>The biggest change in Selenium recently has been the inclusion of the WebDriver API.Driving a browser natively as a user would either locally or on a remote machine using the Selenium Server it marks a leap forward in terms of browser automation.</cite><p>by http://www.seleniumhq.org/projects/webdriver/</p>
					<h4>In this documentation, i use chrome and ChromeDriver of Seleium WebDriver. Under lists, You can read how to use Webdriver for Chrome and download chromedriver. In my case, i downloaded chromedriver version 2.24 </h4>
					<p> - Reference link - </p>
					<ul>
						<ol> Link : https://sites.google.com/a/chromium.org/chromedriver/getting-started</ol>
						<ol> Link : http://chromedriver.storage.googleapis.com/index.html</ol>
					</ul>
					<h4>If you finish to install and download, you unzip chromedriver.zip and move to proper folder and remember the folder path because it's necessary to set the Webdriver file path in script.</h4>
				</li>
			</ol>
		</ol>
	</body>
</html>

