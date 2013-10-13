CSS: style.css

define(`reqdef',`
{#$1}$1
: $2 

[$1]: #$1 "$2"')dnl

define(`tcCount', 0)dnl

define(`tcHeader', `### Test Case $1 ###')dnl
define(`tcdef', `

define(`tcCount', incr(tcCount))dnl

tcHeader(tcCount)

##### Tested Requirements #####

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
<label for="Pass">Pass</label>
<input type="radio" name="tc$1" value="Fail" id="tc$1Fail" checked="false"/>
<label for="Fail">Fail</label>
<input type="radio" name="tc$1" value="Skip" id="tc$1Skip" checked="true"/>
<label for="Skip">Skip</label>
<input type="submit" name="tc$1" value="Save" id="tc$1Save" />
</fieldset>
</form>')dnl

include(title.md)dnl

----
{.breakhere}

include(requirements.md)dnl
include(testcases.md)dnl

----
{.breakhere}
include(signature.md)dnl
