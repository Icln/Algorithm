select i.ITEM_ID, i.ITEM_NAME
from ITEM_INFO i join ITEM_TREE t on i.ITEM_ID = t.ITEM_ID
where t.PARENT_ITEM_ID is null

