'''
Implements a full outer join. Intended to be used within Dataiku where a full outer join is not
supported on the native DSS Engine.
Author: Yash Puranik (yash.puranik@aimpointdigital.com)
Company: Aimpoint Digital, LP
All Rights Reserved
'''
import pandas as pd # type: ignore

def outer_join(left_frame: pd.DataFrame, right_frame: pd.DataFrame, column: str) -> pd.DataFrame:
    '''
    Return a full outer join on a specified column

    Parameters:
    -----------
    left_frame : pd.DataFrame
        Left table for an outer join

    right_frame : pd.DataFrame
        Right  table for an outer join

    column : str
        Column to join on

    Returns:
    --------
    A fully outer joined table
    '''
    return pd.merge(left_frame, right_frame, on=column, how="outer")
