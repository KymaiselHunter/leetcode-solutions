<h3><a href=https://leetcode.com/problems/password-strength/>Password Strength</a></h3>
<p><p>You are given a string <code>password</code>.</p>

<p>The <strong>strength</strong> of the password is calculated based on the following rules:</p>

<ul>
	<li>1 point for each distinct lowercase letter (<code>'a'</code> to <code>'z'</code>).</li>
	<li>2 points for each distinct uppercase letter (<code>'A'</code> to <code>'Z'</code>).</li>
	<li>3 points for each distinct digit (<code>'0'</code> to <code>'9'</code>).</li>
	<li>5 points for each distinct special character from the set <code>"!@#$"</code>.</li>
</ul>

<p>Each character contributes <strong>at most</strong> once, even if it appears multiple times.</p>

<p>Return an integer denoting the strength of the password.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">password = "aA1!"</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The distinct characters are <code>'a'</code>, <code>'A'</code>, <code>'1'</code> and <code>'!'</code>.</li>
	<li>Thus, the <code>strength = 1 + 2 + 3 + 5 = 11</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">password = "bbB11#"</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The distinct characters are <code>'b'</code>, <code>'B'</code>, <code>'1'</code> and <code>'#'</code>.</li>
	<li>Thus, the <code>strength = 1 + 2 + 3 + 5 = 11</code>.​​​​​​​</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= password.length &lt;= 10<sup>5</sup></code></li>
	<li><code>password</code> consists of lowercase and uppercase English letters, digits, and special characters from <code>"!@#$"</code>.</li>
</ul>
</p>
