
def problem1():
    # W = poverty
    # B = business
    # M = microloan

    # P(B | M)
    B_given_M = {'True': 0.85, 
                'False': 0.15}
    # P(B | !M)
    B_given_M_not = {'True': 0.2, 
                    'False': 0.8}
    # P(W | B)
    W_given_B = {'True': 0.01, 
                'False': 0.99}
    # P(W | !B)
    W_given_B_not = {'True': 0.7, 
                    'False': 0.3}

    # P(!W | M) = ((SUMOF(B)) P(M) * P(B | M) * P(W! | B)) / P(M) --> 
    # (SUMOF(B)) P(B | M) * P(!W | B) --> 
    # P(B | M) * P(!W | B) + P(!B | M) * P(!W | !B)

    # P(B | M) * P(!W | B)   +   P(!B | M) * P(!W | B)   +   P(B | M) * P(!W | !B)   +   P(!B | M) * P(!W | !B) --> OR IS IT THIS WHICH IS EVERY COMB.
    W_not_given_M = (B_given_M['True'] * W_given_B['False']) + (B_given_M['False'] * W_given_B_not['False'])


    # P(!W | !M) = P(B | !M) * P(!W | B) + P(!B | !M) * P(!W | !B)
    W_not_given_M_not = (B_given_M_not['True'] * W_given_B['False']) + (B_given_M_not['False'] * W_given_B_not['False'])
    
    print('PROBLEM 1: ', 'P(!W | M):', W_not_given_M, ' & ', 'P(!W | !M):', W_not_given_M_not)


def problem2():
    # W = poverty
    # B = business
    # D = debt / other expenses
    # J = reduced work at wage-paying job
    # M = microloan
    
    # P(B | M)
    B_given_M = {'True': 0.85, 
                'False': 0.15}

    # P(B | !M)
    B_given_M_not = {'True': 0.2, 
                    'False': 0.8}

    # P(J | B)
    J_given_B = {'True': 0.6,
                'False': 0.4}

    # P(J | !B)
    J_given_B_not = {'True': 0.2, 
                    'False': 0.8}
    # P(D | M)
    D_given_M = {'True': 0.75, 
                'False': 0.25}
    # P(D | !M)
    D_given_M_not = {'True': 0.01, 
                    'False': 0.99}

    # P(!W | J, B, D)
    W_not_given_JBD = {'TTT': 0.2,
                        'TTF': 0.5,
                        'TFT': 0.001,
                        'TFF': 0.1,
                        'FTT': 0.35,
                        'FTF': 0.6,
                        'FFT': 0.1,
                        'FFF': 0.5}

    # P(!W | M) = ((SUM(B,J,D)) P(M) * P(B | M) * P(J | B) * P(D | M) * P(!W | J,B,D)) / P(M) -->
    # (SUM(B,J,D)) P(B | M) * P(J | B) * P(D | M) * P(!W | J,B,D) -->

    # B,J,D -> P(B | M) * P(J | B) * P(D | M) * P(!W | J,B,D) +
    # B,J,!D -> P(B | M) * P(J | B) * P(!D | M) * P(!W | J,B,!D) +
    # B,!J,D -> P(B | M) * P(!J | B) * P(D | M) * P(!W | !J,B,D) +
    # B,!J,!D -> P(B | M) * P(!J | B) * P(!D | M) * P(!W | !J,B,!D) +
    # !B,J,D -> P(!B | M) * P(J | !B) * P(D | M) * P(!W | J,!B,D) +
    # !B,J,!D -> P(!B | M) * P(J | !B) * P(!D | M) * P(!W | J,!B,!D) +
    # !B,!J,D -> P(!B | M) * P(!J | !B) * P(D | M) * P(!W | !J,!B,D) +
    # !B,!J,!D -> P(!B | M) * P(!J | !B) * P(!D | M) * P(!W | !J,!B,!D)

    W_not_given_M = ((B_given_M['True'] * J_given_B['True'] * D_given_M['True'] * W_not_given_JBD['TTT']) + 
    (B_given_M['True'] * J_given_B['True'] * D_given_M['False'] * W_not_given_JBD['TTF']) +
    (B_given_M['True'] * J_given_B['False'] * D_given_M['True'] * W_not_given_JBD['FTT']) +
    (B_given_M['True'] * J_given_B['False'] * D_given_M['False'] * W_not_given_JBD['FTF']) +
    (B_given_M['False'] * J_given_B_not['True'] * D_given_M['True'] * W_not_given_JBD['TFT']) +
    (B_given_M['False'] * J_given_B_not['True'] * D_given_M['False'] * W_not_given_JBD['TFF']) +
    (B_given_M['False'] * J_given_B_not['False'] * D_given_M['True'] * W_not_given_JBD['FFT']) +
    (B_given_M['False'] * J_given_B_not['False'] * D_given_M['False'] * W_not_given_JBD['FFF']))

    W_not_given_M_not = ((B_given_M_not['True'] * J_given_B['True'] * D_given_M_not['True'] * W_not_given_JBD['TTT']) + 
    (B_given_M_not['True'] * J_given_B['True'] * D_given_M_not['False'] * W_not_given_JBD['TTF']) +
    (B_given_M_not['True'] * J_given_B['False'] * D_given_M_not['True'] * W_not_given_JBD['FTT']) +
    (B_given_M_not['True'] * J_given_B['False'] * D_given_M_not['False'] * W_not_given_JBD['FTF']) +
    (B_given_M_not['False'] * J_given_B_not['True'] * D_given_M_not['True'] * W_not_given_JBD['TFT']) +
    (B_given_M_not['False'] * J_given_B_not['True'] * D_given_M_not['False'] * W_not_given_JBD['TFF']) +
    (B_given_M_not['False'] * J_given_B_not['False'] * D_given_M_not['True'] * W_not_given_JBD['FFT']) +
    (B_given_M_not['False'] * J_given_B_not['False'] * D_given_M_not['False'] * W_not_given_JBD['FFF']))

    print('PROBLEM 2: ', 'P(!W | M):', W_not_given_M, ' / ', 'P(!W | !M)', W_not_given_M_not)

def problem3():
    # P(SH | S)
    SH_given_S = {'True': 0.8,
                'False': 0.2}
    # P(SH | !S)
    SH_given_S_not = {'True': 0.3,
                    'False': 0.7}
    # P(DVI | SH)
    DVI_given_SH = {'True': 0.75,
                    'False': 0.25}
    # P(DVI | !SH)
    DVI_given_SH_not = {'True': 0.3,
                        'False': 0.7}

    # P(FS | S)
    FS_given_S = {'True': 0.75,
                'False': 0.25}

    # P(FS | !S)
    FS_given_S_not = {'True': 0.1,
                'False': 0.9}

    PPR_given_SH = {'True': 0.9,
                    'False': 0.1}

    PPR_given_SH_not = {'True': 0.3,
                        'False': 0.7}

    # P(IandE | PPR)
    IandE_given_PPR = {'True': 0.8,
                    'False': 0.2}
    # P(IandE | !PPR)
    IandE_given_PPR_not = {'True': 0.4,
                        'False': 0.6}
    # P(ALL | FS)
    ALL_given_FS = {'True': 0.42,
                    'False': 0.58}
    # P(ALL | !FS)
    ALL_given_FS_not = {'True': 0.58,
                        'False': 0.42}
    # P(MP | S)
    MP_given_S = {'True': 0.75,
                    'False': 0.25}
    
    # P(MP | !S)
    MP_given_S_not = {'True': 0.3,
                    'False': 0.7}

    # P(CH | MP)
    CH_given_MP = {'True': 0.7,
                'False': 0.3}
    # P(CH | !MP)
    CH_given_MP_not = {'True': 0.4,
                        'False': 0.6}
    
    # Find P(ALL | Causes??)(True|True) ~= P(ALL | Causes??)(False|True)
    # Find P(ALL | Causes??)(True|True) ~= P(ALL | Causes??)(True|False)
    # P(ALL | S) 
    ALL_given_S = (FS_given_S['True'] * ALL_given_FS['True']) + (FS_given_S['False'] * ALL_given_FS_not['True'])

    # P(!ALL | S)
    ALL_not_given_S = (FS_given_S['True'] * ALL_given_FS['False']) + (FS_given_S['False'] * ALL_given_FS_not['False'])

    # P(ALL | !S)
    ALL_given_S_not = (FS_given_S_not['True'] * ALL_given_FS['True']) + (FS_given_S_not['False'] * ALL_given_FS_not['True'])


    # Find P(IandE | Causes??)(True|True) >> P(IandE | Causes??)(False|True)
    # Find P(IandE | Causes??)(True|True) >> P(IandE | Causes??)(True|False)
    # P(IandE | S)
    IandE_given_S = ((SH_given_S['True'] * PPR_given_SH['True'] * IandE_given_PPR['True']) + 
    (SH_given_S['True'] * PPR_given_SH['False'] * IandE_given_PPR_not['True']) + 
    (SH_given_S['False'] * PPR_given_SH_not['True'] * IandE_given_PPR['True']) + 
    (SH_given_S['False'] * PPR_given_SH_not['False'] * IandE_given_PPR_not['True']))
    
    # P(!IandE | S)
    IandE_not_given_S = ((SH_given_S['True'] * PPR_given_SH['True'] * IandE_given_PPR['False']) + 
    (SH_given_S['True'] * PPR_given_SH['False'] * IandE_given_PPR_not['False']) + 
    (SH_given_S['False'] * PPR_given_SH_not['True'] * IandE_given_PPR['False']) + 
    (SH_given_S['False'] * PPR_given_SH_not['False'] * IandE_given_PPR_not['False']))

    # P(IandE | !S)
    IandE_given_S_not = ((SH_given_S_not['True'] * PPR_given_SH['True'] * IandE_given_PPR['True']) + 
    (SH_given_S_not['True'] * PPR_given_SH['False'] * IandE_given_PPR_not['True']) + 
    (SH_given_S_not['False'] * PPR_given_SH_not['True'] * IandE_given_PPR['True']) + 
    (SH_given_S_not['False'] * PPR_given_SH_not['False'] * IandE_given_PPR_not['True']))

    # Find P(DVI | Causes??)(True|True) << P(DVI | Causes??)(False|True)
    # Find P(DVI | Causes??)(True|True) << P(DVI | Causes??)(True|False)
    # P(DVI | S)
    DVI_given_S = (DVI_given_SH['True'] * SH_given_S['True']) + (DVI_given_SH_not['True'] * SH_given_S['False'])

    # P(!DVI | S)
    DVI_not_given_S = (DVI_given_SH['False'] * SH_given_S['True']) + (DVI_given_SH_not['False'] * SH_given_S['False'])

    # P(DVI | !S)
    DVI_given_S_not = (DVI_given_SH['True'] * SH_given_S_not['True']) + (DVI_given_SH_not['True'] * SH_given_S_not['False'])
    print('PROBLEM 3:')
    print('P(ALL | S) / P(!ALL | S) / P(ALL | !S): ', ALL_given_S, ' / ', ALL_not_given_S, ' / ', ALL_given_S_not)
    print('P(IandE | S) / P(!IandE | S) / P(I&E | !S): ', IandE_given_S, ' / ', IandE_not_given_S, ' / ', IandE_given_S_not)
    print('P(DVI | S) / P(!DVI | S) / P(DVI | !S): ', DVI_given_S, ' / ', DVI_not_given_S, ' / ', DVI_given_S_not)

def summation():
    array = [0.4725, 0.3675, 0.105, 0.0525] 
    matrix = [[0.49, 0.21, 0.21, 0.09], [0.21, 0.49, 0.09, 0.21], [0.21, 0.09, 0.49, 0.21], 
    [0.09, 0.21, 0.21, 0.49]]
    result = [0, 0, 0, 0]

    for i in range(len(array)):
        for j in range(len(matrix)):
            result[j] += (array[j] * matrix[j][i])
            #print(array[j], ' * ', matrix[j][i])
            #print(result[j])
            
    print(result)

summation()
