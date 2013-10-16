define(`reqdef',`
{#$1}$1
: shift($@)

[$1]: #$1 "$*"')dnl

define(`tcCount', 0)dnl
define(`hrPageBreak', `{.page-break}---')dnl

define(`tcHeader', `### Test Case $1 ###')dnl
define(`tcdef', `

define(`tcCount', incr(tcCount))dnl
tcHeader(tcCount)
**Tested Requirements**

$*
resultButtons(tcCount)')dnl

define(`satisfies',`ifelse(eval($#<2),1,`* [$1]',`
* [$1] 
satisfies(shift($@))')')dnl

define(resultButtons,`
<form>
<fieldset>
<legend>Results for Test Case $1</legend>
<input type="radio" name="tc$1" value="Pass" id="tc$1Pass" checked="false"/>
<label for="tc$1Pass">Pass</label>
<input type="radio" name="tc$1" value="Fail" id="tc$1Fail" checked="false"/>
<label for="tc$1Fail">Fail</label>
<input type="radio" name="tc$1" value="Skip" id="tc$1Skip" checked="true"/>
<label for="tc$1Skip">Skip</label>
<input type="submit" value="Save"/><br/>
<textarea rows="5" cols="80" name="tc$1comment"> </textarea><br/> 
</fieldset>
</form>')dnl


