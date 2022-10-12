corrmat = df.drop(['Year', 'Month', 'Day', 'Minute', 'TimeSunRise', 'TimeSunSet'], inplace=False, axis=1)

plt.figure(figsize=(9, 9))
sns.heatmap(corrmat.corr(), annot=True, cmap = sns.dark_palette("#69d", reverse=True, as_cmap=True))
plt.show()

sns.distplot(df['Radiation'])
plt.xlim([df['Radiation'].min(),df['Radiation'].max()])

grouped_m=df.groupby('Month').mean().reset_index()
grouped_h=df.groupby('Hour').mean().reset_index()

f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, sharex='col', sharey='row', figsize=(14,12))

h = grouped_h['Hour']
m = grouped_m['Month']

ax1.grid()
ax1.set_title('Mean Radiation by Hour')
ax1.bar(h, grouped_h['Radiation'])

ax2.grid()
ax2.set_title('Mean Radiation by Month')
ax2.bar(m, grouped_m['Radiation'])

ax3.grid()
ax3.set_title('Mean Temperature by Hour')
ax3.bar(h, grouped_h['Temperature'])

ax4.grid()
ax4.set_title('Mean Temperature by Month')
ax4.bar(m, grouped_m['Temperature'])

ax5.grid()
ax5.set_title('Mean Pressure by Hour')
ax5.bar(h, grouped_h['Pressure'])

ax6.grid()
ax6.set_title('Mean Pressure by Month')
ax6.bar(m, grouped_m['Pressure'])

ax7.grid()
ax7.set_title('Mean Humidity by Hour')
ax7.bar(h, grouped_h['Humidity'])

ax8.grid()
ax8.set_title('Mean Humidity by Month')
ax8.bar(m, grouped_m['Humidity'])

biv = sns.PairGrid(df, vars = ['Radiation','Temperature','Humidity','Pressure'])
biv.map_upper(plt.scatter, s=10)
biv.map_diag(sns.distplot, kde=False)
biv.map_lower(sns.kdeplot, shade=True)

plt.show()
